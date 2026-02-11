#!/usr/bin/env python3

import sys
import os
import subprocess
import json
from pathlib import Path

# ---
# Editable prompt template
# ---
PROMPT_TEMPLATE = """
You are an expert at creating high-engagement social media summaries for community meetings.

Your task:
- Read the transcript below.
- Produce a structured summary designed to encourage attendance at the next meeting.
- Highlight key moments, decisions, and emotional beats.
- Keep the tone energetic, positive, and community‑focused.
- Include 3–5 short, punchy social media posts that could be used on Discord, Slack, and LinkedIn.

Transcript:
\"\"\"
{transcript}
\"\"\"

Now produce the structured summary.
"""

def run_ollama(model: str, prompt: str) -> str:
    """Run an Ollama model with the given prompt and return the output text."""
    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    out, err = process.communicate(prompt)

    if process.returncode != 0:
        raise RuntimeError(f"Ollama error: {err}")
    
    return out

def main():
    if len(sys.argv) < 3:
        print("Usage: summarize.py <transcript.txt> <ollama-model>")
        sys.exit(1)

    transcript_path = Path(sys.argv[1])
    model_name = sys.argv[2]

    if not transcript_path.exists():
        print(f"Error: transcript file not found: {transcript_path}")
        sys.exit(1)

    # Load transcript
    transcript = transcript_path.read_text(encoding="utf-8")

    # Build prompt
    prompt = PROMPT_TEMPLATE.format(transcript=transcript)

    print(f"Running summarization using model: {model_name}")
    summary = run_ollama(model_name, prompt)

    # Output file
    output_path = transcript_path.with_suffix(".summary.txt")
    output_path.write_text(summary, encoding="utf-8")

    print(f"Summary saved to: {output_path}")

if __name__ == "__main__":
    main()