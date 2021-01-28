import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()


def startTalk():
    engine.say("Hay, I am alex")
    engine.say("What can I do for you")
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def runn():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk("current time is" + time)
        url = "https://www.google.com.tr/search?q={}".format("current time")
        webbrowser.open_new_tab(url)
    elif 'weather' in command:
        weather = command.replace('show me the weather in', 'weather in')
        url = "https://www.google.com.tr/search?q={}".format(weather)
        talk("showing weather in" + weather)
        webbrowser.open_new_tab(url)
    elif 'who is' in command:
        try:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        except:
            talk("I couldn't find a wikipedia page on that topic, let's try google search")
            url = "https://www.google.com.tr/search?q={}".format(person)
            webbrowser.open_new_tab(url)
    elif 'what is' in command:
        try:
            thing = command.replace('what is', '')
            info = wikipedia.summary(thing, 1)
            talk(info)
        except:
            talk("I couldn't find a wikipedia page on that topic, let's try google search")
            url = "https://www.google.com.tr/search?q={}".format(thing)
            webbrowser.open_new_tab(url)
    elif 'tell me more about' in command:
        try:
            thing = command.replace('tell me more about', '')
            info = wikipedia.summary(thing, 1)
            talk(info)
        except:
            talk("I couldn't find a wikipedia page on that topic, let's try google search")
            url = "https://www.google.com.tr/search?q={}".format(thing)
            webbrowser.open_new_tab(url)
    elif 'search' in command:
        thing = command.replace('search', '')
        url = "https://www.google.com.tr/search?q={}".format(thing)
        talk("searching" + thing)
        webbrowser.open_new_tab(url)
    else:
        talk("Sorry, that command is a little to much for me right now")
