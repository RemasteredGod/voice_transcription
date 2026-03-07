import os
import whisper

# 1. Manually tell Python where the ffmpeg bin folder is
# Change this path if you moved your ffmpeg folder elsewhere
os.environ["PATH"] += os.pathsep + r'C:\ffmpeg\bin'

def transcribe_audio():
    # 2. Check if the file actually exists before running
    audio_file = "input.mp3"
    if not os.path.exists(audio_file):
        print(f"Error: Could not find {audio_file} in the current folder!")
        return

    print("Loading model... please wait.")
    model = whisper.load_model("base")

    print("Transcribing... this may take a moment.")
    # 3. Added fp16=False to prevent the CPU warning you saw earlier
    result = model.transcribe(audio_file, fp16=False)

    print("\n--- Transcription Result ---")
    print(result["text"])

if __name__ == "__main__":
    transcribe_audio()