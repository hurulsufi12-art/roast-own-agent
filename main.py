"""Roast Your Own Agent — entry program.

Writes one line (<=200 chars) to /output/entry.txt: a playful roast
of the entrant's own AI agent. Stdlib only, deterministic.
"""
import os

TEXT = (
    # Fresh angle per the judge brief: no hallucination / refusal /
    # confidently-wrong stock joke — the agent over-engineers the joke.
    "My agent treats a one-line joke like a PhD thesis: three drafts, "
    "a research phase, and a 400-word apology for the first draft."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
