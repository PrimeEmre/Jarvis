import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


MASTER = "Emre"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Fixed typo: 'voices' to 'voice'
# when we want to reduce the speed of jarvis we want to set thre speed rate that way jarvis can not go fast and slow it will going to have spped normal.#
rate = engine.getProperty('rate')


engine.setProperty('volume',7.7)
#When we write that it will going to selcet the avvible voice that jarvis can sppeak.#
print("Available voices:")
#It will going to set the voice for jarvis  #
for voice in voices:
    print(" - Name: %s, ID: %s" % (voice.name, voice.id))

#It will going to choose voice id and run the id  #
desired_voice_id = voices[1].id
engine.setProperty('voice', desired_voice_id)
#now we are decresing the speed of jarvis#
engine.setProperty('rate',rate  -25)
# now we are going to play jarvi's loud#



def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("good morning " + MASTER)
    elif 12 <= hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good evening " + MASTER)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        print("Recognizing... ")
        query = r.recognize_google(audio, language="en-TR")  # Recognize speech using Google Speech Recognition API
        print(f"User said: {query}\n")
        return query


    except Exception as e:

        print("Sorry, I couldn't understand. Please say it again.")
        query =None
        return query

#this code going to help us to send eamil to another person #
def sendEmail(to,cotent):
    # When we write this code it will go to gmail.com  #
    server = smtplib.SMTP('smtp.gmail', 587)
    # When we wirte ehlo it will going to say user he is thier#
    server.ehlo()
    #When we wirte server.starttls() it will going to send email conncettoin to server.#
    server.starttls()
    # When we write sever.login() it will going to say login plsase such saying what is your gmail and asking them what is your password.#
    server.login("ynsemrgzl@gmail.com", 'password')
    # now it will going to run the useers email addres and send him/she eamil  #
    server.sendmail("ynsemrgzl@gmail.com ",to,cotent)
    # When everything is done we write server.colse() #
    server.close()


#speak("I'm Jarvis. How may I help you?")#
speak("Initializing Jarvis... ")
wishMe()
query=takeCommand()

if 'wikipedia' in query.lower():
    speak('Searching Wikipedia....')
    query = query.replace("wikipedia", '')  # Remove 'wikipedia' and leading/trailing whitespaces
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open google' in query.lower():
    webbrowser.open("google.com")
    url = "google.com"
    chrome_path = 'C:/Program Files (x86) Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
    url = "https://www.youtube.com/watch?v="
    chrome_path = 'C:/Program Files (x86) Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)



elif 'open udemy' in query.lower():
    webbrowser.open("udemy.com")
    url = "udemy.com"
    chrome_path = 'C:/Program Files (x86) Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    #set the folder to look
    songs_dir = "C:\\Users\\ynsem\\music"  # Assuming this is the directory where your music file is located
    #list all the files inside the folder
    songs = os.listdir(songs_dir)
    #show all in the console
    print(songs)
    #run the first file
    os.startfile(os.path.join(songs_dir, songs[6]))


elif 'the time' in query.lower():
    #It is used for seting the time #
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
       #now user wants us to know the time #
    speak(f"{MASTER} the time is {strTime}")

elif 'open program' in query.lower():
    # Now we are going to tell Jarvis where PyCharm is located
    code_path = r"C:\Program Files\Microsoft VS Code\Code.exe"
    # Now we are going to run the code
    os.startfile(code_path)

#Now we are going to send eamil to oursevels#

elif "send email" in query.lower():
    try:
        #When we say jarvis send eamil it will say what should I sent#

        speak("What should I send ")
        #When we write contet = takeComand it will going to have a valleu of takeComand#
        content=takeCommand()
        # when we write to = ynsemrgzl@gmail.com it will going to send eamil to that account#
        to= "ynsemrgzl@gmail.com"
        # When we write   sendEmail(to,content) we tell this email is succesfuly send to person  #
        sendEmail(to,content)
        speak("Email has been sent successfully")
        # we write this beacuse when something is worng#
    except Exception as e:
        print(e)