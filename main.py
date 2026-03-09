import os
import whisper
import shutil

def setup_ffmpeg():
    """Check if ffmpeg is available, if not provide helpful error message"""
    if shutil.which("ffmpeg"):
        print("✓ FFmpeg found in system PATH")
        return True
    
    # Try local project folder first, then common installation locations
    script_dir = os.path.dirname(os.path.abspath(__file__))
    common_paths = [
        os.path.join(script_dir, "ffmpeg", "bin"),  # Local project folder
        os.path.join(script_dir, "ffmpeg"),  # Local project folder (no bin subfolder)
        r'C:\ffmpeg\bin',
        r'C:\Program Files\ffmpeg\bin',
        os.path.join(os.path.expanduser("~"), "ffmpeg", "bin")
    ]
    
    for path in common_paths:
        if os.path.exists(os.path.join(path, "ffmpeg.exe")):
            os.environ["PATH"] += os.pathsep + path
            print(f"✓ FFmpeg found at: {path}")
            return True
    
    print("✗ FFmpeg not found! You have source code but need compiled binaries.")
    print("  Download pre-built ffmpeg from: https://www.gyan.dev/ffmpeg/builds/")
    print("  Extract ffmpeg.exe to: " + os.path.join(script_dir, "ffmpeg", "bin"))
    print("  Or install via: winget install ffmpeg")
    return False

def transcribe_audio():
    # 1. Setup ffmpeg first
    if not setup_ffmpeg():
        return
    
    # 2. Use harvard.wav for transcription
    audio_file = "harvard.wav"
    
    if not os.path.exists(audio_file):
        print(f"Error: Could not find {audio_file} in the current folder!")
        return
    
    print(f"Found audio file: {audio_file}")

    print("Loading model... please wait.")
    model = whisper.load_model("base")

    print("Transcribing... this may take a moment.")
    # 3. Added fp16=False to prevent the CPU warning you saw earlier
    result = model.transcribe(audio_file, fp16=False)

    print("\n--- Transcription Result ---")
    print(result["text"])

if __name__ == "__main__":
    transcribe_audio()