"""Step 2.3: search the FAISS index for the chunks most relevant to a question, one province at a time.

Usage:
    r = Retriever()
    r.search("How much vacation after 5 years?", "Ontario", k=3)

Searching within one province guarantees a comparison question gets evidence from both provinces,
instead of one province's chunks crowding out the other's.
`exclude_sections` removes sections from the results (used later for the missing-evidence demo).
"""
from __future__ import annotations

import sys
from pathlib import Path

import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import load_config  # noqa: E402


class Retriever:
    def __init__(self, cfg: dict | None = None):
        self.cfg = cfg or load_config()
        vs = self.cfg["paths"]["vector_store"]
        self.index = faiss.read_index(str(vs / "faiss.index"))
        self.chunks = pd.read_json(vs / "chunks.jsonl", lines=True, dtype={"section": str})
        self.model = SentenceTransformer(self.cfg["embedding_model"])
        self.rows_by_jur = {j: np.where(self.chunks["jurisdiction"].values == j)[0]
                            for j in self.chunks["jurisdiction"].unique()}

    def search(self, question: str, jurisdiction: str, k: int | None = None,
               exclude_sections: set[str] | None = None) -> pd.DataFrame:
        """Top-k chunks for one province, best first. Columns include rank, score, chunk_id, section, label, text."""
        k = k or self.cfg["retrieval"]["top_k"]
        if jurisdiction not in self.rows_by_jur:          # e.g. Alberta: nothing in the knowledge base
            return self.chunks.head(0).assign(rank=[], score=[])
        q = self.model.encode([question], normalize_embeddings=True, convert_to_numpy=True).astype(np.float32)
        scores, rows = self.index.search(q, self.index.ntotal)  # exact scores for every chunk (fast at this size)
        allowed = set(self.rows_by_jur[jurisdiction])
        hits = [(r, s) for r, s in zip(rows[0], scores[0]) if r in allowed]
        res = self.chunks.iloc[[r for r, _ in hits]].copy()
        res["score"] = [round(float(s), 4) for _, s in hits]
        if exclude_sections:
            res = res[~res["section"].isin(exclude_sections)]
        res = res.head(k).reset_index(drop=True)
        res.insert(0, "rank", range(1, len(res) + 1))
        return res
