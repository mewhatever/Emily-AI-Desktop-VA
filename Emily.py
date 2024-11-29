import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser

engine = pyttsx3.init()

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.setProperty('rate', 170)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause duration before ending input
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Timeout and phrase time limit
            print("Recognizing...")

            query = r.recognize_google(audio, language='en-US')  # Change 'en-US' to 'en-IN' for Indian English
            print(f"You said: {query}\n")

        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return "None"

        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
            return "None"

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
            return "None"

        except Exception as e:
            print(f"An error occurred: {e}")
            return "None"
    return query

if __name__ == "__main__":

    print("Speaking...")
    speak("Hello, Nabin! This is Emily. What can I do for you, sir?")

    while True:
        query = takeCommand().lower()

    # noinspection PyUnreachableCode
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open('https://www.google.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'stop' in query or 'exit' in query:
            speak("Goodbye, Nabin! Have a good day sir!")
            break

    # if command != "None":
    #     speak(f"You said: {command}")
