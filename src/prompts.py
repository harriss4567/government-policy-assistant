"""Prompt templates shared by fine-tuning (training data) and inference (the pipeline).

Keeping them in one place guarantees the model sees the same instructions in training and at test
time, and that every experiment (A–E) uses identical prompts.
"""
from __future__ import annotations

NS = "Not specified in the excerpt"

ACT_NAMES = {
    "Ontario": "Employment Standards Act, 2000 (Ontario)",
    "British Columbia": "Employment Standards Act (British Columbia)",
}

SYSTEM_PROMPT = (
    "You extract employment-standards requirements from legislative excerpts. "
    "Use only the excerpts provided. Answer with a single JSON object with exactly these keys: "
    "jurisdiction, topic, section, eligibility, entitlement_or_requirement, threshold, exceptions, "
    "mandatory, supporting_quote. "
    f'Write "{NS}" for any field the excerpts do not state; never guess. '
    "exceptions is a list (empty if none are stated). "
    f'mandatory is "mandatory" if the excerpt binds someone (shall / must / must not / may not / is entitled to), '
    f'"optional" if it only permits something (may), or "{NS}" for definitions, scope statements or no answer. '
    "supporting_quote is copied word for word from an excerpt, or an empty string if no excerpt answers the question."
)


def format_excerpt(i: int, jurisdiction: str, section: str, text: str) -> str:
    return f"[{i}] {ACT_NAMES[jurisdiction]}, s. {section}:\n{text}"


def build_user_prompt(jurisdiction: str, question: str, excerpts: list[tuple[str, str]]) -> str:
    """excerpts: list of (section, text) for the given jurisdiction."""
    blocks = "\n\n".join(format_excerpt(i, jurisdiction, sec, txt) for i, (sec, txt) in enumerate(excerpts, 1))
    return (f"Jurisdiction: {jurisdiction}\n"
            f"Question: {question}\n\n"
            f"Excerpts:\n{blocks}\n\n"
            "Fill in the JSON using only these excerpts.")


# ---- No-RAG prompt (experiments A, C, F): same JSON form, but answered from the model's own knowledge ----
SYSTEM_PROMPT_NO_RAG = (
    "You answer questions about employment-standards legislation from your own knowledge. "
    "Answer with a single JSON object with exactly these keys: "
    "jurisdiction, topic, section, eligibility, entitlement_or_requirement, threshold, exceptions, "
    "mandatory, supporting_quote. "
    f'Write "{NS}" for any field you do not know; never guess. '
    "exceptions is a list (empty if none). "
    f'mandatory is "mandatory", "optional", or "{NS}". '
    "supporting_quote is an empty string, because no excerpts are provided."
)


def build_user_prompt_no_rag(jurisdiction: str, question: str) -> str:
    return (f"Jurisdiction: {jurisdiction}\n"
            f"Question: {question}\n\n"
            f"No excerpts are provided. Fill in the JSON from your own knowledge of the {ACT_NAMES[jurisdiction]}.")


# ---- Relevance check: do the retrieved excerpts actually answer the question? ----
RELEVANCE_SYSTEM = "You check whether legal excerpts contain the answer to a question. Reply with only YES or NO."
_EXTRACT_INSTRUCTION = "Fill in the JSON using only these excerpts."


def build_relevance_prompt(user_prompt: str, jurisdiction: str) -> str:
    """Reuse the extraction prompt (question + excerpts) and swap the final instruction for a YES/NO question.
    The question is scoped to one province, so a comparison question ("Toronto vs Vancouver?") isn't rejected
    just because one province's excerpts can't answer the whole comparison."""
    return user_prompt.replace(_EXTRACT_INSTRUCTION,
                               f"Considering only {jurisdiction}, do these excerpts contain the information needed "
                               f"to answer the question for {jurisdiction}? Reply YES or NO.")
