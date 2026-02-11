#!/usr/bin/env python3

import sys
import whisper
import os
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 transcribe.py <video-file>")
        sys.exit(1)

    video_path = Path(sys.argv[1])

    if not video_path.exists:
        print(f"Error: file not found: {video_path}")
        sys.exit(1)

    print("Loading Whisper large-v3 model...")
    model = whisper.load_model("large-v3")

    print(f"Transcribing: {video_path.name}")
    result = model.transcribe(str(video_path))

    output_path = video_path.with_suffix(".txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcript saved to: {output_path}")

if __name__ == "__main__":
    main()