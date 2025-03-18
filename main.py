from vosk import Model, KaldiRecognizer
import wave
import os
import sys
# if path to file is not specified will prompt instruction on how to use program
if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_wave_file>")
        sys.exit(1)
# Load Persian model
try:
    model = Model("model-fa")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Open the WAV file for reading
wav_path = sys.argv[1]
if not os.path.exists(wav_path):
    print(f"File not found: {wav_path}")
    exit(1)

try:
    with wave.open(wav_path, "rb") as wf:
        # Initialize the recognizer with the model and sample rate
        rec = KaldiRecognizer(model, wf.getframerate())

        # Process the audio frames in a loop
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print(rec.Result())

        # Print the final transcription result
        print(rec.FinalResult())
except Exception as e:
    print(f"Error processing WAV file: {e}")
