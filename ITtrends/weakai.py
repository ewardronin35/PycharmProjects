import wikipediaapi
import speech_recognition as sr
import cv2
import numpy as np

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')


# Function to search and retrieve Wikipedia content
def get_wikipedia_summary(topic):
    page = wiki_wiki.page(topic)
    if page.exists():
        return page.summary
    else:
        return "Sorry, I couldn't find information about that."


# Function for speech recognition
def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return ""


# Function to detect a hand using a webcam
def detect_hand():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Convert the frame to grayscale for better hand detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use a hand detection algorithm (e.g., Haar Cascade Classifier or a deep learning model)
        # In this example, we're using a simple contour-based method for demonstration purposes.
        ret, thresholded = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 10000:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 3)
                cv2.putText(frame, "Hand Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Hand Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        user_input = speech_recognition()
        if "search" in user_input:
            search_topic = user_input.replace("search", "").strip()
            result = get_wikipedia_summary(search_topic)
            print(result)
        elif "hand" in user_input:
            detect_hand()
        elif "exit" in user_input:
            break
