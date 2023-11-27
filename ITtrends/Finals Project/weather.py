import requests
from tkinter import Tk, Label, Entry, Button
from gtts import gTTS
from playsound import playsound

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Change this to 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_weather_and_speak(api_key, city):
    weather_data = get_weather(api_key, city)
    if weather_data['cod'] == '404':
        speak("City not found. Please check the city name.")

    else:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        message = f"The weather in {city} is {description} with a temperature of {temperature} degrees Celsius."
        speak(message)

def speak(message):
    tts = gTTS(message, lang='en')
    tts.save('output.mp3')
    playsound('output.mp3')

def on_submit():
    city = entry.get()
    get_weather_and_speak(api_key, city)


api_key = '8b7ad73934fc4708bbe131936232511'

# Create GUI
root = Tk()
root.title("Weather App")

label = Label(root, text="Enter city:")
label.pack()

entry = Entry(root)
entry.pack()

submit_button = Button(root, text="Get Weather", command=on_submit)
submit_button.pack()

root.mainloop()
