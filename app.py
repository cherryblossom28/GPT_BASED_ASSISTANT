from openai import OpenAI
from apikey import api_data 
import os
import speech_recognition as sr  # Converts voice commands to text
import pyttsx3  # Converts text output to voice
import webbrowser 

Model = "gpt-3.5-turbo"  # Make sure this is available in your API key
client = OpenAI(api_key=api_data)

def Reply(question):
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role': "system", "content": "You are a helpful assistant"},
            {'role': 'user', 'content': question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message.content
    return answer

# Text-to-speech setup for macOS (female English voice)
engine = pyttsx3.init()  # macOS uses nsss engine by default
voices = engine.getProperty('voices')

# Set voice to female English (usually the second voice in macOS)
female_voice = None
for voice in voices:
    if 'female' in voice.name.lower() and 'english' in voice.languages[0].lower():
        female_voice = voice
        break

if female_voice:
    engine.setProperty('voice', female_voice.id)
else:
    print("Female English voice not found, using default.")

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initial greeting
speak("Hello, how are you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening .......')
        r.pause_threshold = 1  # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try:
        print('Recognizing ....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again .....")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue

        ans = Reply(query)
        print(ans)
        speak(ans)

        # Specific Browser Related Tasks
        if "open youtube" in query:
            webbrowser.open('https://www.youtube.com')
        if "open google" in query:
            webbrowser.open('https://www.google.com')
        if "bye" in query:
            speak("Goodbye!")
            break