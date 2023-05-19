import speech_recognition as sr
import pyttsx3




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:

        with sr.Microphone() as Source:
            print("Listen")
            voice = listener.listen(Source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'ronin' in command:
                command = command.replace('ronin', '')
                print(command)
    except:
        pass
    return command

def run_ronin():
    command = take_command()
    print(command)
    if 'play' in command:
        talk('playing')
        print('playing')

run_ronin()