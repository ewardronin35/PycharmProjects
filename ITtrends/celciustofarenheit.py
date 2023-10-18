import pyttsx3
from gtts import gTTS
import os

engine = pyttsx3.init()

print("Welcome to simple program")


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to speak a given text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Get Celsius temperature from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius} Degrees Celsius ay equal sa {fahrenheit:.2f} degrees Fahrenheit")

# Convert the result to text
result_text = f"{celsius} Ang Degrees Celsius daw ay equal sa {fahrenheit:.2f} Degrees Fahrenheit"
engine.say(f"{celsius} Ang Degrees Celsius daw ay equal sa {fahrenheit:.2f} Degrees Fahrenheit")
engine.runAndWait()

# Use gTTS to generate speech from the text
tts = gTTS(text=result_text, lang='tl')

# Save the speech to an audio file
tts.save("result.mp3")

# Play the audio file
os.system("result.mp3")
