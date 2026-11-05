"""Step 3.5: the question-answering pipeline, built as a LangChain chain of five steps.

    question
      │ 1. route      which provinces is the question about? (Ontario, BC, or one we don't cover)
      │ 2. answer     per province: retrieve top-k chunks → prompt → model → JSON (one retry)
      │               → verify (quote really in the law? cited section really retrieved?)
      │               → relevance check (do the excerpts answer the question at all?) → abstain if not
      │ 3. compare    if two provinces answered: same / different, decided in code (not by the model)
      │ 4. render     plain-text answer with citations, warnings, and the required licence notices
      ▼
    result dict: answer text + a full trace (retrieved chunks, raw model output, checks, tokens, seconds)

Experiments (configs/config.yaml → experiments): A–F choose the model, adapter on/off, and RAG on/off.
Everything else (prompts, retrieval, checks, rendering) is identical across experiments.

Usage:
    from pipeline import Pipeline
    p = Pipeline("D")
    print(p.run("How much vacation do I get after 6 years in Toronto vs Vancouver?")["answer"])
"""
from __future__ import annotations

import difflib
import json
import re
import sys
from pathlib import Path

from langchain_core.runnables import RunnableLambda

sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm  # noqa: E402
from config import load_config  # noqa: E402
from prompts import (ACT_NAMES, NS, RELEVANCE_SYSTEM, SYSTEM_PROMPT, SYSTEM_PROMPT_NO_RAG,  # noqa: E402
                     build_relevance_prompt, build_user_prompt, build_user_prompt_no_rag)
from retrieval import Retriever  # noqa: E402

KEYS = ["jurisdiction", "topic", "section", "eligibility", "entitlement_or_requirement", "threshold",
        "exceptions", "mandatory", "supporting_quote"]
SHORT = {"Ontario": "ON", "British Columbia": "BC"}

# ---- 1. routing: which provinces does the question mention? ----
PLACES = {
    "Ontario": ["ontario", "toronto", "ottawa", "mississauga", "brampton", "hamilton", "kitchener", "waterloo",
                "windsor", "london, on", "sudbury", "kingston"],
    "British Columbia": ["british columbia", "bc", "b.c.", "vancouver", "victoria", "surrey", "burnaby",
                         "richmond", "kelowna", "kamloops", "nanaimo"],
}
OTHER_PLACES = {
    "Alberta": ["alberta", "calgary", "edmonton"], "Quebec": ["quebec", "québec", "montreal", "montréal"],
    "Manitoba": ["manitoba", "winnipeg"], "Saskatchewan": ["saskatchewan", "regina", "saskatoon"],
    "Nova Scotia": ["nova scotia", "halifax"], "New Brunswick": ["new brunswick", "fredericton", "moncton"],
    "Newfoundland and Labrador": ["newfoundland", "labrador"], "Prince Edward Island": ["prince edward island", "pei"],
    "Yukon": ["yukon"], "Northwest Territories": ["northwest territories"], "Nunavut": ["nunavut"],
}


def _mentions(text: str, words: list[str]) -> bool:
    return any(re.search(rf"(?<![a-z]){re.escape(w)}(?![a-z])", text) for w in words)


def route(question: str) -> dict:
    q = question.lower()
    covered = [j for j, words in PLACES.items() if _mentions(q, words)]
    other = [j for j, words in OTHER_PLACES.items() if _mentions(q, words)]
    note = None
    if not covered and not other:
        covered, note = list(PLACES), "No province was named, so both Ontario and British Columbia are shown."
    return {"covered": covered, "not_covered": other, "note": note}


# ---- helpers for step 2 ----
def parse_json(text: str) -> dict | None:
    m = re.search(r"\{.*\}", text, flags=re.S)
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def quote_found(quote: str, passages: list[str], fuzzy_min: float) -> bool:
    """Exact match ignoring case/spacing, else the best same-length window must be >= fuzzy_min similar."""
    q = _norm(quote)
    for p in map(_norm, passages):
        if q in p:
            return True
        n = len(q)
        for i in range(0, max(1, len(p) - n + 1), 5):
            if difflib.SequenceMatcher(None, q, p[i:i + n]).ratio() >= fuzzy_min:
                return True
    return False


def base_sections(section: str) -> set[str]:
    return {re.sub(r"\(.*", "", s).strip().removeprefix("s.").strip() for s in str(section).split(",") if s.strip()}


def is_abstain(ans: dict) -> bool:
    return str(ans.get("entitlement_or_requirement", NS)).startswith("Not specified") or \
        str(ans.get("section", NS)).startswith("Not specified")


# ---- 3. comparison in code ----
NUMBER_WORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                "eight": "8", "nine": "9", "ten": "10", "twelve": "12", "half": "0.5"}


def numbers(text: str) -> set[str]:
    t = _norm(text)
    for w, d in NUMBER_WORDS.items():
        t = re.sub(rf"\b{w}\b", d, t)
    return set(re.findall(r"\d+(?:\.\d+)?%?", t))


def compare(results: list[dict]) -> dict | None:
    answered = [r for r in results if r["status"] == "answered"]
    if len(results) < 2:
        return None
    if len(answered) < 2:
        return {"verdict": "unknown", "reason": "At least one province's answer is not specified in the retrieved law."}
    a, b = (r["answer"] for r in answered[:2])
    fields = {}
    for f in ("entitlement_or_requirement", "threshold", "eligibility"):
        x, y = str(a.get(f, NS)), str(b.get(f, NS))
        if x.startswith("Not specified") or y.startswith("Not specified"):
            fields[f] = "unknown"
        elif numbers(x) or numbers(y):
            fields[f] = "same" if numbers(x) == numbers(y) else "different"
        else:
            fields[f] = "same" if _norm(x) == _norm(y) else "different wording (check details)"
    known = [v for v in fields.values() if v != "unknown"]
    verdict = "different" if "different" in known else "same" if known and all(v == "same" for v in known) \
        else "unclear"
    return {"verdict": verdict, "fields": fields}


# ---- 4. rendering ----
NOTICES = {
    "general": "Not legal advice. This is a research prototype; check the official legislation or an employment "
               "standards office before relying on it.",
    "Ontario": "Ontario legislation: © King's Printer for Ontario, 2000. This is not an official version. "
               "The official version is available on e-Laws at https://www.ontario.ca/laws.",
    "British Columbia": "These materials contain information that has been derived from information originally made "
                        "available by the Province of British Columbia at: http://www.bclaws.gov.bc.ca and this "
                        "information is being used in accordance with the King's Printer Licence – British Columbia "
                        "available at: https://www.bclaws.gov.bc.ca/standards/Licence.html. They have not, however, "
                        "been produced in affiliation with, or with the endorsement of, the Province of British "
                        "Columbia and THESE MATERIALS ARE NOT AN OFFICIAL VERSION.",
}
LABELS = {"eligibility": "Who it applies to", "threshold": "Amount / threshold", "mandatory": "Mandatory?"}


def render(state: dict) -> str:
    lines = []
    if state["route"]["note"]:
        lines.append(state["route"]["note"])
    for r in state["results"]:
        j, ans = r["jurisdiction"], r.get("answer") or {}
        lines.append(f"\n{j.upper()}: {ACT_NAMES[j]}" + (f", s. {ans.get('section')}" if r["status"] == "answered" else ""))
        if r["status"] != "answered":
            lines.append(f"  Not specified in the retrieved sections. {r['reason']}")
            continue
        lines.append(f"  Answer: {ans.get('entitlement_or_requirement')}")
        for f, label in LABELS.items():
            v = ans.get(f)
            if v and not str(v).startswith("Not specified"):
                lines.append(f"  {label}: {v}")
        if ans.get("exceptions"):
            lines.append("  Exceptions: " + "; ".join(map(str, ans["exceptions"])))
        if ans.get("supporting_quote"):
            lines.append(f'  Quote: "{ans["supporting_quote"]}"')
        if r.get("source_url"):
            lines.append(f"  Source: {r['source_url']}")
        for w in r["warnings"]:
            lines.append(f"  ⚠ {w}")
    for j in state["route"]["not_covered"]:
        lines.append(f"\n{j.upper()}: not covered. This tool only includes the Ontario and British Columbia "
                     "Employment Standards Acts, so it cannot answer for this province.")
    if state.get("comparison"):
        c = state["comparison"]
        lines.append(f"\nCOMPARISON: {c['verdict'].upper()}")
        if c.get("fields"):
            lines += [f"  {f.replace('_', ' ')}: {v}" for f, v in c["fields"].items()]
        if c.get("reason"):
            lines.append(f"  {c['reason']}")
    lines.append("\n" + NOTICES["general"])
    lines += [NOTICES[r["jurisdiction"]] for r in state["results"]]
    return "\n".join(lines)


class Pipeline:
    def __init__(self, experiment: str = "D", cfg: dict | None = None):
        self.cfg = cfg or load_config()
        self.exp_name = experiment
        self.exp = self.cfg["experiments"][experiment]
        self.model = self.cfg["models"][self.exp["model"]]
        self.retriever = Retriever(self.cfg) if self.exp["rag"] else None
        self.chain = (RunnableLambda(self._route) | RunnableLambda(self._answer_all)
                      | RunnableLambda(self._compare) | RunnableLambda(self._render))

    # LangChain steps (each takes and returns the running "state" dict)
    def _route(self, inp: dict) -> dict:
        return {**inp, "route": route(inp["question"])}

    def _answer_all(self, s: dict) -> dict:
        return {**s, "results": [self.answer_one(s["question"], j, s.get("exclude", {}).get(j))
                                 for j in s["route"]["covered"]]}

    def _compare(self, s: dict) -> dict:
        return {**s, "comparison": compare(s["results"])}

    def _render(self, s: dict) -> dict:
        return {**s, "answer": render(s)}

    def run(self, question: str, exclude: dict[str, set[str]] | None = None) -> dict:
        """exclude: sections to hide from retrieval per province, e.g. {"British Columbia": {"40"}} (failure demo)."""
        out = self.chain.invoke({"question": question, "exclude": exclude or {}})
        out["experiment"] = {"name": self.exp_name, **self.exp, "model_id": self.model["id"]}
        out["totals"] = {k: sum(c.get(k, 0) for r in out["results"] for c in r["calls"])
                         for k in ("prompt_tokens", "output_tokens", "seconds")}
        return out

    # step 2, for one province
    def answer_one(self, question: str, jurisdiction: str, exclude: set[str] | None = None) -> dict:
        gen, pcfg = self.cfg["generation"], self.cfg["pipeline"]
        use_adapter = self.exp["adapter"]
        r = {"jurisdiction": jurisdiction, "retrieved": [], "calls": [], "warnings": [], "checks": {}}

        if self.retriever:
            hits = self.retriever.search(question, jurisdiction, exclude_sections=exclude)
            r["retrieved"] = hits[["rank", "score", "chunk_id", "section", "label", "text", "source_url"]] \
                .to_dict(orient="records")
            user = build_user_prompt(jurisdiction, question, [(h["label"], h["text"]) for h in r["retrieved"]])
            system = SYSTEM_PROMPT
        else:
            user, system = build_user_prompt_no_rag(jurisdiction, question), SYSTEM_PROMPT_NO_RAG
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user}]

        # model → JSON, with one retry if the JSON is invalid or the keys are wrong
        ans = None
        for attempt in range(1 + gen["retries"]):
            out = llm.chat(self.model["id"], msgs, self.model["adapter"], use_adapter, gen["max_new_tokens"])
            r["calls"].append({"step": "extract", "attempt": attempt + 1, **out})
            ans = parse_json(out["text"])
            if ans is not None and set(ans) == set(KEYS):
                break
            msgs = msgs + [{"role": "assistant", "content": out["text"]},
                           {"role": "user", "content": "That was not a valid JSON object with exactly the 9 keys. "
                                                       "Reply with only the JSON object."}]
        r["checks"]["valid_json"] = ans is not None
        r["checks"]["exact_keys"] = ans is not None and set(ans) == set(KEYS)
        r["checks"]["retries"] = len([c for c in r["calls"] if c["step"] == "extract"]) - 1
        if ans is None:
            return {**r, "status": "failed", "answer": None,
                    "reason": "The model did not return a usable answer (invalid JSON after a retry)."}
        default = {"supporting_quote": "", "exceptions": []}           # a missing key means "nothing given"
        ans = {k: ans.get(k, default.get(k, NS)) for k in KEYS}
        r["answer"] = ans

        # verification (only possible when there are excerpts)
        if self.retriever:
            passages = [h["text"] for h in r["retrieved"]]
            q = str(ans.get("supporting_quote") or "")
            r["checks"]["quote"] = "empty" if not q else \
                "verified" if quote_found(q, passages, pcfg["quote_fuzzy_min"]) else "not found"
            cited = base_sections(ans["section"]) - {"Not specified in the excerpt"}
            got = {h["section"] for h in r["retrieved"]}
            r["checks"]["section"] = "none" if not cited else "verified" if cited <= got else "not retrieved"
            if r["checks"]["quote"] == "not found":
                r["warnings"].append("The quote could not be found in the retrieved law. Treat this answer with caution.")
            if r["checks"]["section"] == "not retrieved":
                r["warnings"].append(f"Cited section {ans['section']} was not among the retrieved sections.")
            urls = {h["section"]: h["source_url"] for h in r["retrieved"]}
            r["source_url"] = next((urls[s] for s in cited if s in urls), None)
        else:
            r["checks"]["quote"] = r["checks"]["section"] = "no excerpts (not verifiable)"
            r["warnings"].append("Answered without retrieving the law (no-RAG experiment): citations are unverified.")

        if is_abstain(ans):
            return {**r, "status": "abstained", "reason": "The retrieved law does not state this; it may be set out "
                                                          "in regulations, which this tool does not include."}

        # relevance check: do the excerpts actually answer the question?
        if self.retriever and pcfg["relevance_check"]:
            rel_msgs = [{"role": "system", "content": RELEVANCE_SYSTEM},
                        {"role": "user", "content": build_relevance_prompt(user, jurisdiction)}]
            judge = self.cfg["models"][pcfg["relevance_model"]]      # same judge for every experiment
            rel = llm.yes_probability(judge["id"], rel_msgs, judge["adapter"], use_adapter=False)
            r["calls"].append({"step": "relevance", **rel})
            r["checks"]["relevance_p_yes"] = rel["p_yes"]
            if rel["p_yes"] < pcfg["relevance_min_p_yes"]:
                return {**r, "status": "abstained",
                        "reason": "The retrieved sections don't appear to answer this question (relevance check)."}
        return {**r, "status": "answered"}
