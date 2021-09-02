import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from flask_mail import Mail
import subprocess, sys


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[12].id)  #changing index, changes voices. [0] for male

rate = engine.getProperty('rate')   # getting details of current speaking rate
# print(rate)                        #printing current voice rate
engine.setProperty('rate', 140)    # setting up new voice rate

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print(volume)                          #printing current volume level
engine.setProperty('volume', 2.0)    # setting up volume level  between 0 and 1


def speak(audio):
    """
    This function takes a string as an arguement
    :param audio: string
    :return:
    """
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """
    This function wish the user as per the current time
    :return:
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning sir")

    elif 12 <= hour < 18:
        speak("Good afternoon sir")

    else:
        speak("Good evening sir")

    speak("I am Jarvis")
    speak(" how may I help you")


def TakeCommand():
    """
    It take command from user by using microphone of device
    :return: User input/command
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        speak("Can't reconizing, say again please...")
        return "none"
    return query


def SendMail(to, content):
    """
    it takes Two arguements as input and send the email to given id
    :param to: Email id
    :param content: content to write in mail
    :return:
    """
    server = smtplib.SMTP('smtp.gmail.com', 587) #host − This is the host running your SMTP server. You can specify IP address of the host or a domain name like tutorialspoint.com. 587 ia a port no of gmail.com.
    server.ehlo()
    server.starttls()
    server.login('omkardannak2003@gmail.com', 'Anita@2452000')
    server.sendmail('omkardannak2003@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    dic = {"omkar": "omkardannak24@gmail.com", "mukunda": "mmhasalkar@gmail.com"}
    wishme()
    while True:
        query = TakeCommand().lower()
        if 'email to' in query:
            try:
                # content_id = TakeCommand()
                to = query.split("to")
                to = to[1]
                to = dic[to]
                # print(dannak)
                speak('What should I say?')
                content_m = TakeCommand()
                SendMail(to, content_m)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry my friend omkar. I am not able to send this email")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = '/home/omkar223/Omkar/Study/Programming/Python/Music'
            songs = os.listdir(music_dir)
            print(songs)
            file_path = (os.path.join(music_dir, songs[1]))
            # print(file_path)
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, file_path])

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)





