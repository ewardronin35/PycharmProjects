import cv2
import speech_recognition as sr
from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Create a tkinter window
root = tk.Tk()
root.title("Assistive Technology for Visually Impaired")

# Create a label to display computer vision results
label = ttk.Label(root, text="Computer Vision Results")
label.pack()

def start_listening():
    # Capture audio input and convert it to text
    with sr.Microphone() as source:
        label.config(text="Listening...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        label.config(text="You said: " + recognized_text)

        # Perform actions based on recognized text (e.g., read text aloud)
        if "read" in recognized_text:
            text_to_read = "This is a test message for the visually impaired."
            tts = gTTS(text_to_read)
            tts.save("output.mp3")
            os.system("mpg123 output.mp3")

    except sr.UnknownValueError:
        label.config(text="Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        label.config(text=f"Could not request results from Google Speech Recognition service; {e}")

    root.after(1000, start_listening)  # Continuously listen

# Create a button to start listening
listen_button = ttk.Button(root, text="Start Listening", command=start_listening)
listen_button.pack()

def update_frame():
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display the computer vision results on the screen
    cv2.imshow("Assistive Technology for Visually Impaired", frame)

    root.after(10, update_frame)

update_frame()

root.mainloop()

# Release the webcam and close OpenCV window
cap.release()
cv2.destroyAllWindows()
