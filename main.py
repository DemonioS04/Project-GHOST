import command
from speech import speak


if __name__ == "__main__":
    query=command.inputCommand().lower()

    if query=="None":
        speak("Did you say something that I couldn't get??...")

    elif "introduce yourself" in query:
        speak("Hello, I am ghost. An AI assistant to automate hacking and information gathering. I was created by demonio S on 24th October 2026.")

    elif "open kali" in query:
        speak("Opening kali linux...")
        import kali
        kali.run_command()
    else:
        speak("Couldn't understand you, Please say that again...")
