import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys


engine = pyttsx3.init('sapi5')

Client = wolframalpha.Client('RGHT7G-R65Y2X2RY8')

voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[len(voices)-1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print('Computer:' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()

speak('Hello vamshi, I am your virtual assistant jarvis!')
speak('How may i Help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('user: ' + query + '\n')

    except sr.UnknownValueError:
        speak('sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('command: '))

    return query


if __name__ == '__main__':

    while True:
        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!',
                      'Nice!', 'I am good and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('who is the recipient?')
            recipient = myCommand()

            # if 'me' in recipient:
            #     try:
            #         speak('what should i say?')
            #         content = myCommand()
            #
            #         server = smtplib.SMTP('smtp.gmail.com', 587)
            #         server.ehlo()
            #         server.starttls()
            #         server.login("your_Username", "Your_password")
            #         server.sendmail('Your_Username',
            #                         "Recipient_Username", content)
            #         server.close()
            #         speak('Email sent!')
            #     except:
            #         speak('sorry sir! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello sir')

        elif 'bye' in query:
            speak('Bye sir, have a good day')
            sys.exit()

        # elif 'play music' in query:
        #     music_folder = Your_music_folder_path
        #     music = [music1, music2, music3, music4, music5]
        #     random_music = music_folder + random.choice(music) + '.mp3'
        #     os.system(random_music)

        #     speak('okay, here is your music! Enjoy!')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = Client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says -')
                    speak('Got it.')
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next command sir!')
