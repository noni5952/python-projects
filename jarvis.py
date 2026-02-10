import datetime
import webbrowser
import random

def speak(text):
    print("JARVIS:", text)

def get_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def get_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {date}")

def calculate(expression):
    try:
        result = eval(expression)
        speak(f"The answer is {result}")
    except:
        speak("Sorry, I can't calculate that.")

def tell_joke():
    jokes = [
        "Why did the computer get tired? Because it ran too many programs.",
        "Why was the math book sad? Because it had too many problems.",
        "I would tell you a joke about Python, but it's too interpreted."
    ]
    speak(random.choice(jokes))

def main():
    speak("Hello! I am your mini JARVIS.")
    
    while True:
        command = input("You: ").lower()

        if "time" in command:
            get_time()

        elif "date" in command:
            get_date()

        elif "calculate" in command:
            expression = command.replace("calculate", "")
            calculate(expression)

        elif "joke" in command:
            tell_joke()

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "exit" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
