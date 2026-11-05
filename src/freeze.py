"""Day 4: freeze the pipeline before the full test run.

"Freezing" = recording a fingerprint (SHA-256 hash) of everything that can change a result: code, settings,
prompts, test set, rubric, search index, LoRA adapter, model versions and library versions.
The full run (run_experiments.py --tag full) checks the fingerprint first and refuses to start if anything
changed, so every reported number comes from exactly this frozen system.

Usage:
    .venv/bin/python src/freeze.py           # create results/freeze_manifest.json
    .venv/bin/python src/freeze.py --check   # compare the current files with the manifest
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime
from importlib.metadata import version
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT, load_config  # noqa: E402

MANIFEST = ROOT / "results/freeze_manifest.json"
FILES = (["app.py", "configs/config.yaml", "requirements.txt", "docs/rubric.md", "data/evaluation.jsonl",
          "vector_store/faiss.index", "vector_store/chunks.jsonl",
          "models/lora-adapter/adapter_model.safetensors", "models/lora-adapter/adapter_config.json"]
         + sorted(str(p.relative_to(ROOT)) for p in (ROOT / "src").glob("*.py")))
LIBS = ["torch", "transformers", "peft", "sentence-transformers", "faiss-cpu", "langchain-core"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def model_revision(model_id: str) -> str | None:
    """The exact Hugging Face snapshot (commit hash) cached locally for this model."""
    ref = Path.home() / ".cache/huggingface/hub" / f"models--{model_id.replace('/', '--')}" / "refs/main"
    return ref.read_text().strip() if ref.exists() else None


def fingerprint() -> dict:
    cfg = load_config()
    models = {m["id"]: model_revision(m["id"]) for m in cfg["models"].values()}
    models[cfg["embedding_model"]] = model_revision(cfg["embedding_model"])
    return {"files": {f: sha256(ROOT / f) for f in FILES},
            "models": models,
            "libraries": {lib: version(lib) for lib in LIBS}}


def check() -> list[str]:
    """Return a list of differences between now and the manifest (empty = frozen state intact)."""
    if not MANIFEST.exists():
        return ["no freeze manifest: run src/freeze.py first"]
    frozen, now = json.loads(MANIFEST.read_text()), fingerprint()
    diffs = []
    for group in ("files", "models", "libraries"):
        for k in sorted(set(frozen[group]) | set(now[group])):
            if frozen[group].get(k) != now[group].get(k):
                diffs.append(f"{group}: {k} changed")
    return diffs


def main():
    if "--check" in sys.argv:
        diffs = check()
        print("FROZEN STATE INTACT" if not diffs else "CHANGED SINCE FREEZE:\n  " + "\n  ".join(diffs))
        sys.exit(1 if diffs else 0)
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "src", "app.py", "configs"], cwd=ROOT,
                               capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        commit, dirty = None, ""
    manifest = {"frozen_at": datetime.now().isoformat(timespec="seconds"), "git_commit": commit,
                "uncommitted_code_changes": bool(dirty), **fingerprint()}
    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"Frozen at {manifest['frozen_at']} · git {commit[:7] if commit else 'n/a'}"
          f"{' (WARNING: uncommitted code changes)' if dirty else ''} · {len(manifest['files'])} files, "
          f"{len(manifest['models'])} models, {len(manifest['libraries'])} libraries\nWrote {MANIFEST}")


if __name__ == "__main__":
    main()
