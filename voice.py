import speech_recognition as sr
import operator
import pyaudio
r = sr.Recognizer()
# open the file
def num1():
    global text
    with sr.Microphone() as source:
        print("Enter the first number: ")
        r.adjust_for_ambient_noise(source)
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=3)
        print("Recognizing...")
        # convert speech to text
        text = int(r.recognize_google(audio_data))
        print(text)
        return text
num1()
def num2():
    global text1
    with sr.Microphone() as source1:
        print("Enter the second number: ")
        r.adjust_for_ambient_noise(source1)
        # read the audio data from the default microphone
        audio_data1 = r.record(source1, duration=3)
        print("Recognizing...")
        # convert speech to text
        text1 = int(r.recognize_google(audio_data1))
        print(text1)
        return text1
num2()
def oppy():
    global opp
    with sr.Microphone() as source2:
        print("What operation do you want to? (+, -, *, /): ")
        r.adjust_for_ambient_noise(source2)
        # read the audio data from the default microphone
        audio_data2 = r.record(source2, duration=3)
        print("Recognizing...")
        # convert speech to text
        opp = r.recognize_google(audio_data2)
        print(opp)
        while True:
            if opp == "division":
                print(text, "/", text1, "=", text / text1)
                break
            elif opp == "addition":
                print(text, "+", text1, "=", text + text1)
                break
            elif opp == "subtraction":
                print(text, "-", text1, "=", text - text1)
                break
            elif opp == "into":
                print(text, "*", text1, "=", text * text1)
                break
            else:
                print("please try again.")
                break




oppy()


