# vosk-farsi
Vosk is an offline speech recognition toolkit that works with multiple languages, including Persian (Farsi). It uses deep learning-based models to transcribe audio into text without needing an internet connection.
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
How vosk works:
1. Install Vosk & Dependencies:
    Create a Python Virtual Enviroment and run: pip install vosk
2. You need a pre-trained model.
    You can download it from:https://alphacephei.com/vosk/models
    for it to run with this script it has to be called "model-fa" after extraction.
3. Prepare audio: 
    Vosk works best with 16kHz mono WAV files
4. Run the Transcription Script:
    Usage: python3 main.py <path_to_wave_file>