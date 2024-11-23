import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        speak("Listening for a command.")
        try:
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("I couldn't understand that.")
            return None
        except sr.RequestError:
            speak("Network error.")
            return None
        except sr.WaitTimeoutError:
            speak("You took too long to respond.")
            return None

def main():
    manager = FileManager()
    speak("Welcome to the voice-based file manager.")
    
    while True:
        speak("What would you like to do? You can say list files, search files, move a file, copy a file, delete a file, or exit.")
        command = listen_command()
        
        if command is None:
            continue

        if "list files" in command:
            speak("Please provide the directory path.")
            directory = listen_command()
            if directory:
                files = manager.list_files(directory)
                speak("Here are the files:")
                for file in files:
                    speak(file)

        elif "search files" in command:
            speak("Please provide the directory path.")
            directory = listen_command()
            speak("What pattern should I search for? For example, star dot txt for all text files.")
            pattern = listen_command()
            if directory and pattern:
                matches = manager.search_files(directory, pattern)
                speak("Here are the matching files:")
                for match in matches:
                    speak(match)

        elif "move file" in command:
            speak("Please provide the source file path.")
            src = listen_command()
            speak("Please provide the destination file path.")
            dest = listen_command()
            if src and dest:
                result = manager.move_file(src, dest)
                speak(result)

        elif "copy file" in command:
            speak("Please provide the source file path.")
            src = listen_command()
            speak("Please provide the destination file path.")
            dest = listen_command()
            if src and dest:
                result = manager.copy_file(src, dest)
                speak(result)

        elif "delete file" in command:
            speak("Please provide the file path to delete.")
            path = listen_command()
            if path:
                result = manager.delete_file(path)
                speak(result)

        elif "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    main()
