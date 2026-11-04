"""Step 2.4: measure retrieval on the 30 test questions (Recall@k), before any LLM is involved.

Definition (rubric §5): for each question × jurisdiction with gold sections, Recall@k = share of its gold
sections that appear among that jurisdiction's top-k retrieved chunks; averaged over all pairs.
Matching is at section level (a chunk of s. 22(7) counts for gold section s. 22).
Alberta (Q29) has no gold sections and is skipped.

Writes results/retrieval_metrics.json: overall, by category, by phrasing, and every miss at k = top_k.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import load_config  # noqa: E402
from retrieval import Retriever  # noqa: E402


def evaluate(retriever: Retriever | None = None, cfg: dict | None = None, save: bool = True):
    cfg = cfg or load_config()
    retriever = retriever or Retriever(cfg)
    ks = cfg["retrieval"]["eval_k"]
    top_k = cfg["retrieval"]["top_k"]
    questions = [json.loads(l) for l in open(cfg["paths"]["evaluation"], encoding="utf-8")]

    rows = []
    for q in questions:
        for jur, g in q["gold"].items():
            gold = set(g["sections"])
            res = retriever.search(q["question"], jur, k=max(ks))
            row = {"id": q["id"], "category": q["category"], "phrasing": q["phrasing"], "jurisdiction": jur,
                   "question": q["question"], "gold": sorted(gold),
                   "retrieved": [f"{l} ({s:.2f})" for l, s in zip(res["label"], res["score"])],
                   "top1_score": float(res["score"].iloc[0]) if len(res) else None}
            for k in ks:
                found = set(res.head(k)["section"]) & gold
                row[f"recall@{k}"] = len(found) / len(gold)
            rows.append(row)

    df = pd.DataFrame(rows)
    rcols = [f"recall@{k}" for k in ks]
    summary = {
        "pairs_scored": len(df),
        "overall": df[rcols].mean().round(3).to_dict(),
        "by_category": df.groupby("category")[rcols].mean().round(3).to_dict(orient="index"),
        "by_phrasing": df.groupby("phrasing")[rcols].mean().round(3).to_dict(orient="index"),
        "by_jurisdiction": df.groupby("jurisdiction")[rcols].mean().round(3).to_dict(orient="index"),
        "misses_at_top_k": df[df[f"recall@{top_k}"] < 1][["id", "jurisdiction", "question", "gold", "retrieved"]]
                           .to_dict(orient="records"),
        "settings": {"embedding_model": cfg["embedding_model"], "top_k": top_k,
                     "max_chars": cfg["chunking"]["max_chars"]},
    }
    if save:
        Path(cfg["paths"]["retrieval_metrics"]).write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    return summary, df


if __name__ == "__main__":
    s, _ = evaluate()
    print(json.dumps({k: s[k] for k in ("pairs_scored", "overall", "by_phrasing")}, indent=2))
    print(f"misses at k={s['settings']['top_k']}: {len(s['misses_at_top_k'])}")
