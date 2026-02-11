# vidsum

A local‑first, GPU‑accelerated pipeline for turning long community meeting videos into
high‑quality, social‑media‑ready summaries.

This project uses:

- **Whisper large‑v3 (Python)** for accurate transcription  
- **Ollama** for structured summarization  
- **Prompt‑driven templates** for generating engaging posts that encourage attendance at future meetings  

Everything runs locally — no cloud APIs, no external dependencies.

---

## Features

- Fast, GPU‑accelerated transcription using Whisper large‑v3  
- Clean `.txt` transcript output for downstream processing  
- Prompt‑driven summarizer script using any Ollama model  
- Structured summaries designed for social media engagement  
- Fully local, reproducible workflow  

---

## Requirements

- Python 3.14  
- PyTorch 2.10+ with CUDA  
- FFmpeg installed and available on PATH  
- Ollama installed with at least one model pulled (e.g., `llama3.1:8b`, `deepseek-r1:14b`)  

---

## Transcription

Use `transcribe.py` to convert any video or audio file into a text transcript.

```bash
./transcribe.py path/to/video.mp4
```
This produces:
```bash
path/to/video.txt
```

The script automatically uses Whisper large-v3 and your GPU.

## Summarization

Uses `summarize.py` to turn a transcript into a structured, social-media-ready summary.

```bash
./summarize.py path/to/video.txt your_model_choice
```

This produces:
```bash
path/to/video.summary.txt
```

The summarizer uses a prompt template inside the script that you can freely modify to tune tone,
structure, and messaging.

## Workflow Example

```bash
./transcribe.py meeting.mp4
./summarize.py meeting.txt llama3.1:8b
```

Output:
- `meeting.txt` - full transcript
- `meeting.summary.txt` - structured summary + social media posts

## Project Structure
```
vidsum/
|- transcribe.py
|- summarize.py
|- requirements.txt
|- README.md
|- LICENSE
-- .gitignore
```

## License

MIT License