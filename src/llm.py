"""Load the local models once and run them: chat (JSON answers) and yes/no questions (relevance check).

- Models run on the M1 GPU (MPS) in float16, or on CUDA / CPU if that's what's available.
- Qwen is loaded once WITH its LoRA adapter. "Base" experiments (A, B) switch the adapter off for the call
  (`disable_adapter`), so base and fine-tuned use exactly the same weights apart from the adapter.
- Greedy decoding (no sampling): the same input always gives the same output.
- Every call returns the text plus prompt/output token counts and seconds, for the latency/tokens metrics.
"""
from __future__ import annotations

import contextlib
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")          # all models are already in the local cache

import torch  # noqa: E402
from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import ROOT  # noqa: E402

DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
_LOADED: dict[str, tuple] = {}


def load(model_id: str, adapter: str | None = None):
    """Return (tokenizer, model), loading on first use. The adapter (if any) is attached once."""
    if model_id not in _LOADED:
        tok = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.float16).to(DEVICE)
        if adapter:
            from peft import PeftModel
            model = PeftModel.from_pretrained(model, str(ROOT / adapter)).to(DEVICE)
        _LOADED[model_id] = (tok, model.eval())
    return _LOADED[model_id]


def _adapter_ctx(model, use_adapter: bool):
    """Switch the LoRA adapter off for base-model calls; no-op when there is no adapter."""
    if not use_adapter and hasattr(model, "disable_adapter"):
        return model.disable_adapter()
    return contextlib.nullcontext()


def chat(model_id: str, messages: list[dict], adapter: str | None = None, use_adapter: bool = False,
         max_new_tokens: int = 400) -> dict:
    tok, model = load(model_id, adapter)
    inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt",
                                     return_dict=True).to(DEVICE)
    t0 = time.perf_counter()
    with torch.no_grad(), _adapter_ctx(model, use_adapter):
        out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False,
                             pad_token_id=tok.pad_token_id or tok.eos_token_id)
    new = out[0, inputs["input_ids"].shape[1]:]
    return {"text": tok.decode(new, skip_special_tokens=True), "prompt_tokens": int(inputs["input_ids"].shape[1]),
            "output_tokens": int(len(new)), "seconds": round(time.perf_counter() - t0, 2)}


def yes_probability(model_id: str, messages: list[dict], adapter: str | None = None,
                    use_adapter: bool = False) -> dict:
    """P(YES) vs. P(NO) for the model's first answer word, read from its next-token scores (no text generated)."""
    tok, model = load(model_id, adapter)
    inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt",
                                     return_dict=True).to(DEVICE)
    yes_id = tok.encode("YES", add_special_tokens=False)[0]
    no_id = tok.encode("NO", add_special_tokens=False)[0]
    t0 = time.perf_counter()
    with torch.no_grad(), _adapter_ctx(model, use_adapter):
        logits = model(**inputs).logits[0, -1]
    p_yes, p_no = torch.softmax(logits[[yes_id, no_id]].float(), dim=0).tolist()
    return {"p_yes": round(p_yes, 4), "answer": "YES" if p_yes >= p_no else "NO",
            "prompt_tokens": int(inputs["input_ids"].shape[1]), "seconds": round(time.perf_counter() - t0, 2)}
