import pyttsx3
from gtts import gTTS
import os


print("Welcome to simple program")
# Function to convert Celsius to Fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit * 9/5) + 32

# Function to speak a given text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def voice_recognition():
    return
# Get Celsius temperature from the user
fahrenheit = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
celcius = fahrenheit_to_celsius(fahrenheit)

# Display the result
print(f"{fahrenheit} degrees Celsius is equal to {celcius:.2f} degrees Fahrenheit")

# Convert the result to text
result_text = f"{fahrenheit} degrees Celsius is equal to {celcius:.2f} degrees Fahrenheit"

# Use gTTS to generate speech from the text
tts = gTTS(text=result_text, lang='tl')

# Save the speech to an audio file
tts.save("result.mp3")

# Play the audio file
os.system("result.mp3")
