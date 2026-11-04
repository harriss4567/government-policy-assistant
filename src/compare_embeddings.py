"""Compare embedding models for retrieval on NON-test questions (no tuning on the test set).

Questions: the 20 validation examples (primary) and, as a larger check, the 80 training examples.
Gold = the base section(s) in each example's expected JSON; examples whose answer is
"Not specified in the excerpt" have no gold section and are skipped.
The live vector_store/ is not touched: each model's index is built in memory.

Usage:  .venv/bin/python src/compare_embeddings.py
Writes: results/embedding_comparison.json
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunking import build_chunks  # noqa: E402
from config import load_config  # noqa: E402

MODELS = {
    "all-MiniLM-L6-v2 (baseline)": ("sentence-transformers/all-MiniLM-L6-v2", ""),
    "bge-small-en-v1.5": ("BAAI/bge-small-en-v1.5", "Represent this sentence for searching relevant passages: "),
}
KS = [1, 3, 5]


def load_questions(path: Path) -> list[dict]:
    out = []
    for line in open(path, encoding="utf-8"):
        ex = json.loads(line)
        user = ex["messages"][1]["content"]
        ans = json.loads(ex["messages"][2]["content"])
        if ans["section"].startswith("Not specified"):
            continue
        gold = {re.sub(r"\(.*", "", s.strip()) for s in ans["section"].split(",")}
        out.append({"id": ex["id"], "jurisdiction": ans["jurisdiction"],
                    "question": re.search(r"Question: (.+)", user).group(1), "gold": gold})
    return out


def evaluate(model_id: str, prefix: str, chunks: pd.DataFrame, sets: dict[str, list[dict]]) -> dict:
    t0 = time.perf_counter()
    model = SentenceTransformer(model_id)
    vecs = model.encode(chunks["embed_text"].tolist(), batch_size=64, normalize_embeddings=True,
                        convert_to_numpy=True).astype(np.float32)
    index = faiss.IndexFlatIP(vecs.shape[1])
    index.add(vecs)
    build_s = time.perf_counter() - t0
    jur = chunks["jurisdiction"].values
    result = {"model_id": model_id, "dimensions": int(vecs.shape[1]), "build_seconds": round(build_s, 1)}
    for name, qs in sets.items():
        q = model.encode([prefix + x["question"] for x in qs], normalize_embeddings=True,
                         convert_to_numpy=True).astype(np.float32)
        scores, rows = index.search(q, index.ntotal)
        rec = {k: [] for k in KS}
        misses = []
        for x, r in zip(qs, rows):
            secs = [chunks["section"].iat[i] for i in r if jur[i] == x["jurisdiction"]][:max(KS)]
            for k in KS:
                rec[k].append(len(set(secs[:k]) & x["gold"]) / len(x["gold"]))
            if rec[3][-1] < 1:
                misses.append({"id": x["id"], "gold": sorted(x["gold"]), "top3": secs[:3]})
        result[name] = {"n": len(qs), **{f"recall@{k}": round(float(np.mean(v)), 3) for k, v in rec.items()},
                        "misses_at_3": misses}
    return result


def main():
    cfg = load_config()
    chunks = build_chunks(cfg, save=False)
    root = Path(cfg["paths"]["kb_chunks"]).parents[2]
    sets = {"val": load_questions(root / "data/val.jsonl"), "train": load_questions(root / "data/train.jsonl")}
    report = {name: evaluate(mid, pre, chunks, sets) for name, (mid, pre) in MODELS.items()}
    out = root / "results/embedding_comparison.json"
    out.write_text(json.dumps(report, indent=2))
    for name, r in report.items():
        print(f"\n{name}  ({r['dimensions']}-dim, index built in {r['build_seconds']}s)")
        for s in sets:
            m = r[s]
            print(f"  {s:5} n={m['n']:3}  R@1 {m['recall@1']:.3f}  R@3 {m['recall@3']:.3f}  R@5 {m['recall@5']:.3f}"
                  f"  misses@3: {[x['id'] for x in m['misses_at_3']]}")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
