import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)



def speak(text):
    print(f"GHOST: {text}")
    engine.say(text)
    engine.runAndWait()


# speak("hello world")
    
    
