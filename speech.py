import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the speech assistant function
def speech_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        # Listen for user input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        # Process user input and generate a response
        response = process_input(text)
        
        # Speak the response
        speak(response)
        
    except sr.UnknownValueError:
        print("Oops! Unable to recognize speech.")
    except sr.RequestError as e:
        print("Oops! Could not request results from Google Speech Recognition service; {0}".format(e))

# Define a function to process user input and generate a response
def process_input(input_text):
    if "hello" in input_text.lower():
        return "Hello! How can I assist you?"
    elif "time" in input_text.lower():
        # You can add code here to get the current time
        return "The current time is..."
    elif "search" in input_text.lower():
        search_query = input_text.lower().replace("search", "").strip()
        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            return f"Searching for {search_query}..."
        else:
            return "What would you like me to search for?"
    elif "exit" in input_text.lower():
        exit()
    else:
        return "Sorry, I didn't understand. Can you please repeat that?"

# Define a function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Run the speech assistant
while True:
    speech_assistant()
