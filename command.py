import speech_recognition as sr
from speech import speak

def inputCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"MASTER: {query}\n")
    except Exception as e:
        return "None"
    return query