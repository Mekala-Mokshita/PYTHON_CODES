import sounddevice as sd
import wavio
import speech_recognition as sr

def record_audio(duration=5, filename="output.wav"):
    samplerate = 44100
    print("Recording...")
    data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, data, samplerate, sampwidth=2)
    print(f"Audio saved as {filename}")

def speech_to_text(filename="output.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Text:", text)
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition")

# Run it
record_audio(5)  # Record 5 seconds
speech_to_text()

