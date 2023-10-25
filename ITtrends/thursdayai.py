import wikipediaapi
import speech_recognition as sr
import pyttsx3
import datetime

# Initialize Wikipedia API with a user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='ThursdayAI/1.0'
)

# Initialize the speech recognition
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
text_to_speech = pyttsx3.init()

# Function to get a Wikipedia summary
def get_wikipedia_summary(topic):
    page = wiki_wiki.page(topic)
    if page.exists():
        return page.summary
    else:
        return "Sorry, I couldn't find information about that."

# Function to speak the response
def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()

# Listen for the wake-up call
def listen_for_wake_word():
    while True:
        with sr.Microphone() as source:
            print("Listening for the wake-up call...")
            audio = recognizer.listen(source)

        try:
            wake_word = recognizer.recognize_google(audio).lower()
            if "thursday" in wake_word:
                speak("How can I assist you?")
                break
        except sr.UnknownValueError:
            continue

# Command recognition
listen_for_wake_word()

while True:
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")

        if "tell me about" in command:
            topic = command.replace("tell me about", "").strip()
            summary = get_wikipedia_summary(topic)
            print(summary)
            speak(summary)
        elif "what's the time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"The current time is {current_time}")
            speak(f"The current time is {current_time}")
        elif "stop" in command:
            speak("Goodbye!")
            break
        elif "who are you" in command:
            speak("Hello! I am Thursday, your personal assistant.")
        elif "there is nothing we can't do" in command:
            speak("There is nothing we can't do")

    except sr.UnknownValueError:
        speak("I couldn't understand your command.")
    except sr.RequestError:
        speak("Sorry, I couldn't request results from the speech recognition service.")
