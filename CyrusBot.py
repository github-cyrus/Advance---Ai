import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import openai
# import google
import os
import smtplib
from apikey import api_data
from api_key import API_KEY
from playsound import playsound
openai.api_key=api_data

completion=openai.Completion()



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Cyrus. Sir Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def Reply(question):
    prompt=f'Cyrus: {question}\n Cyrus: '
    response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Cyrus'], max_tokens=200)
    answer=response.choices[0].text.strip()
    return answer




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        ans=Reply(query)
        print(ans)
        speak(ans)

        if 'call jadu' in query:
            speak('Calling Jadu ...')
            playsound('C:\\Users\\Admin\\Downloads\\Compressed\\CyrusBot-AI-main\\CyrusBot-AI-main\\tune (1).mp3')
            # music_dir = 'tune (1).mp3'
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))
            speak('Jadu Sending Message To Cyrus ....')
            playsound('C:\\Users\\Admin\\Downloads\\Compressed\\CyrusBot-AI-main\\CyrusBot-AI-main\\tune (2).mp3')
            speak('Jadu Coming On Monday')


        elif 'open Youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif ' your name' in query:
            speak('My Name is Cyrus')

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open my website' in query:
            webbrowser.open("https://github-cyrus.github.io/Cyrus/")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Admin\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'Which std you study' in query:
            speak('Cyrus Studying in Bsc Data Science')

        

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\itcha\\Downloads\\Projects-main\\Projects-main\\CyrusBot.py"
            os.startfile(codePath)


        elif 'cyrus stop now' in query:
            speak("ok sir,")
            speak( " Cyrus Can i going for sleep now")
            if 'no' in query:
                speak("Ok Im Here Cyrus")
            elif 'ok go' in query:
                speak("Thank you Byy Cyrus Love You")
                exit()

 