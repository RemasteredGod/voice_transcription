# Voice Transcription with Whisper

A simple voice transcription tool using OpenAI's Whisper model with bundled FFmpeg.

## Features
- 🎙️ Transcribe audio files to text using Whisper AI
- 📦 FFmpeg binaries included (no separate installation needed)
- 🔍 Automatic FFmpeg detection and setup
- 🎯 Easy to use

## Installation

1. Clone this repository:
```bash
git clone https://github.com/RemasteredGod/voice_transcription.git
cd voice_transcription
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install openai-whisper
```

## Usage

1. Place your audio file in the project directory (currently using `harvard.wav`)

2. Run the transcription:
```bash
python main.py
```

The script will:
- ✓ Automatically detect FFmpeg (bundled in `ffmpeg/bin/`)
- ✓ Load the Whisper model
- ✓ Transcribe your audio file
- ✓ Display the transcription result

## Supported Audio Formats

- WAV
- MP3
- M4A
- FLAC
- And other formats supported by FFmpeg

## Example Output

```
✓ FFmpeg found at: E:\project\voice_transcription\ffmpeg\bin
Found audio file: harvard.wav
Loading model... please wait.
Transcribing... this may take a moment.

--- Transcription Result ---
The stale smell of old beer lingers. It takes heat to bring out the odor...
```

## Requirements

- Python 3.7+
- openai-whisper
- FFmpeg (included in repository via Git LFS)

## Notes

- First run will download the Whisper model (~140MB)
- FFmpeg executables are tracked with Git LFS
- Git LFS is required to clone the repository with FFmpeg binaries

## License

This project uses:
- OpenAI Whisper (MIT License)
- FFmpeg (GPL/LGPL License)
