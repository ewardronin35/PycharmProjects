import pyttsx3
import cv2



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def add(x, y):
    result = x + y
    speak(f"The sum of {x} and {y} is {result}")
    return result


def subtract(x, y):
    result = x - y
    speak(f"The difference between {x} and {y} is {result}")
    return result


def multiply(x, y):
    result = x * y
    speak(f"The product of {x} and {y} is {result}")
    return result


def divide(x, y):
    if y == 0:
        speak("Error! Division by zero is not allowed.")
        return None
    result = x / y
    speak(f"{x} divided by {y} is {result}")
    return result


while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    choice = input("Enter your choice: ").lower()

    if choice == "exit":
        speak("Goodbye!")
        break

    if choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "add":
            add(num1, num2)
        elif choice == "subtract":
            subtract(num1, num2)
        elif choice == "multiply":
            multiply(num1, num2)
        elif choice == "divide":
            divide_result = divide(num1, num2)
            if divide_result is not None:
                print(f"Result: {divide_result}")
    else:
        speak("Invalid input! Please choose a valid option.")
