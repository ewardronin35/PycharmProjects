import cv2
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the video capture device (usually your webcam)
cap = cv2.VideoCapture(0)  # Change the index if necessary

# Load the pre-trained hand detection model
hand_cascade = cv2.CascadeClassifier(r'C:\Users\eduar\OneDrive\Documents\PycharmProjects\ITtrends\haarcascade_hand.xml')


while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        continue

    # Convert the frame to grayscale for hand detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands in the frame
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If hands are detected, say "Hand detected"
    if len(hands) > 0:
        engine.say("Hand detected")
        engine.runAndWait()

    # Display the video frame
    cv2.imshow('Hand Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
