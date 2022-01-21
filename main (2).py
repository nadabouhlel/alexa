import speech_recognition as sr
import pyttsx3 #so alexa can talk to me
import pywhatkit
import datetime
import wikipedia
import pyjokes


#creating a recognizer to recognize my voice
listener = sr.Recognizer()
engine=pyttsx3.init()
#change alexa voice [0]pour fr [1]pour ang
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
      engine.say(text)
      engine.runAndWait()


#we use the try expressions because somtimes we may face microphone problems
def take_command():
          try:
              with sr.Microphone() as source:
                  print('listening...')
                  voice = listener.listen(source)
                  command = listener.recognize_google(voice)
                  command = command.lower()
                  if 'alexa' in command:
                      command = command.replace('alexa', '')
                      print(command)
          except:
              pass
          return command

def run_alexa():
    command= take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is' + time)
    elif 'search for' in command:
        information = command.replace('search for','')
        info = wikipedia.summary(information,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'do you love me' in command:
        talk('yes of course')
    else:
        talk('please say the command again')

while True:
    run_alexa()