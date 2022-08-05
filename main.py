import time
import speech_recognition as sr
from gtts import gTTS
import pyaudio
r = sr.Recognizer()
# open the file
def voice():
    global text
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=3)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        return text

covidism = 0
print("This is my COVID-19 Detection chatbot to verify whether you are covid positive or not.")
time.sleep(2)
q1 = input("Are you feeling feverish and/or sick? \n You: ")
if q1 == "yes":
    print("Okay, next question.")
    covidism += 1
elif q1 == "no":
    print("Okay next question.")
q2 = input("Are you feeling sore or tired and are you have difficulty breathing? \n You: ")
if q2 == "yes":
    print("Okay, test complete.")
    covidism += 1
elif q2 == "no":
    print("Okay, test complete.")

if covidism == 2:
    print("You are showing all the symptoms for COVID-19 so you are 100% positive.")
elif covidism == 1:
    print("You are showing some of the symptoms for COVID-19. You may be positive or you might have a normal fever.")
else:
    print("You are showing no symptoms of COVID-19. You are 100% negative.")
