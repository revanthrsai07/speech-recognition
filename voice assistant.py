import speech_recognition as sr  # for recognizing speech
import pyttsx3                   # for text to speech conversion
import pywhatkit                 # for opening urls
import datetime                  # for date and time
import wikipedia                 # for searching 
import pyjokes                   # for jokes



# listener is a person who is there to recognize our speech
# super is our AI  
listener = sr.Recognizer()
alexa = pyttsx3.init()


# for setting female voice for our assistant
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

# setting voice rate for the female voice
voice_rate = 178
alexa.setProperty("rate", voice_rate)

# talk function to say what we said to super
def talk(parameterized_text):
    alexa.say(parameterized_text)
    alexa.runAndWait()


"""
1. Computer hears our voice with the help of microphone which acts
as a source. 
2. so the listener listens our voice and converts it into text with the 
help google translator API
3. We can specify one name for our AI, to respond for that specific name only,
   in our case, it is 'Super'
"""
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
        
    except:
        pass 
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk('Current time is' + time)
    elif 'who is' or 'what is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        talk(jokes)
        print(jokes)
    else:
        talk("sorry i could not recognize you")
        

while True:
    run_alexa()