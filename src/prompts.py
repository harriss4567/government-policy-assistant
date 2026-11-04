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
