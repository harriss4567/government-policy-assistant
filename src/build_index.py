"""Step 2.2: embed every chunk and store the vectors in a FAISS index (the vector database).

- Model: configs/config.yaml -> embedding_model (all-MiniLM-L6-v2, 384-dimensional vectors).
- Vectors are normalized, so inner product = cosine similarity (1.0 = identical meaning).
- FAISS IndexFlatIP does exact search, which is fine for ~1,600 chunks.
- Writes vector_store/faiss.index, vector_store/chunks.jsonl (row i of the index = line i), and
  vector_store/index_info.json (model, counts, build time) for the infrastructure slide.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import faiss
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import load_config  # noqa: E402


def build_index(cfg: dict | None = None) -> dict:
    cfg = cfg or load_config()
    out_dir = cfg["paths"]["vector_store"]
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = pd.read_json(cfg["paths"]["kb_chunks"], lines=True, dtype={"section": str})

    t0 = time.perf_counter()
    model = SentenceTransformer(cfg["embedding_model"])
    vectors = model.encode(chunks["embed_text"].tolist(), batch_size=64, normalize_embeddings=True,
                           show_progress_bar=False, convert_to_numpy=True).astype(np.float32)
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)
    seconds = time.perf_counter() - t0

    faiss.write_index(index, str(out_dir / "faiss.index"))
    chunks.to_json(out_dir / "chunks.jsonl", orient="records", lines=True, force_ascii=False)
    info = {
        "embedding_model": cfg["embedding_model"],
        "dimensions": int(vectors.shape[1]),
        "chunks": int(index.ntotal),
        "by_jurisdiction": chunks["jurisdiction"].value_counts().to_dict(),
        "build_seconds": round(seconds, 1),
        "device": str(model.device),
        "index_mb": round((out_dir / "faiss.index").stat().st_size / 1e6, 2),
    }
    (out_dir / "index_info.json").write_text(json.dumps(info, indent=2))
    return info


if __name__ == "__main__":
    print(json.dumps(build_index(), indent=2))
