import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb


friday = pyttsx3.init()
voices = friday.getProperty("voices")
friday.setProperty("voice", voices[1].id)

def speak(audio):
    print("F.R.I.D.A.Y: " + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak("It is")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Sorry, It's time to sleep!")
    speak("How can I help you, boss")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1.5
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language="en-US")
        print("vanhaito: " + query)
    except sr.UnknownValueError:
        print("Sorry sir! I didn\'t get that! Please try typing the command!")
        query = str(input("Your order is: "))
    return query

if __name__ == '__main__':
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search on google, boss")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        elif "youtube" in query:
            speak("What should I search on youtube, boss")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "quit" in query:
            speak("Friday is off. Goodbye boss")
            quit()
        elif "time" in query:
            time()

