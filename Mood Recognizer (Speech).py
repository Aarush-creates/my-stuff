import time
import speech_recognition as sr
from operator import itemgetter
r = sr.Recognizer()

print("This is my program to detect what mood your current mood is. Please answer the following questions.")
def voice():
    global text
    angry = 0
    fear = 0
    happy = 0
    sad = 0
    surprise = 0
    neutral = 0
    hapwrds = ['great', 'amazing', 'fantastic', 'fabulous', 'happy', 'very', 'good']
    sadwrds = ['okay', 'bad', 'depressing', 'sucks', 'boring', 'sad', 'very', 'bored']
    angwrds = ['bad', 'trash', 'horrible', 'sucks', 'annoyed', 'angry', 'very', 'annoyed', 'furious', 'aggravated', 'frustrated']
    neutwrds = ['nothing', 'meh', 'confused', 'cool', 'neutral', 'very', 'good']
    fearwrds = ['scared', 'concerned', 'terrified', 'afraid', 'horrified', 'wary', 'skeptical', 'weird', 'very']
    list = [angry, fear, happy, sad, neutral]
    #
    #
    with sr.Microphone() as source:
        time.sleep(2)
        #
        #
        print("What is your name?\nYou: ")
        q1 = r.record(source, duration=3)
        text = r.recognize_google(q1)
        print("Hello,", text)
        #
        #
        print("How is your day so far?\nYou: ")
        q2 = r.record(source, duration=5)
        text = r.recognize_google(q2)
        print(text)
        for i in text.split():
            if i in hapwrds:
                print("That's great to hear!")
                happy += 1
            elif i in sadwrds:
                print("That sucks, I hope your day gets better.")
                sad += 1
            elif i in angwrds:
                print("That sucks, I hope your day gets better.")
                angry += 1
            elif i in neutwrds:
                print("That's alright!")
            elif i in fearwrds:
                print("Ah I see, I hope your day gets better.")
        time.sleep(3)
        print("Next question.")
        time.sleep(1)
        print("If a stranger came up to you and asked you what you were doing in an aggressive manner, how would you feel?\nYou: ")
        q3 = r.record(source, duration=11)
        text = r.recognize_google(q3)
        print(text)
        for x in text.split():
            if x in hapwrds:
                print("Nice! Let's move on.")
                happy += 1
            elif x in sadwrds:
                print("Interesting. Let's move on.")
                sad += 1
            elif x in angwrds:
                print("Interesting, let's move on")
                angry += 1
            elif x in neutwrds:
                print("Hm, Let's move on.")
                neutral += 1
            elif x in fearwrds:
                print("Interesting. Let's move on.")
                fear += 1
        time.sleep(3)
        print("Next question.")
        time.sleep(1)
        print("You go to school, but none of your friends are there with you. How do you feel?\nYou: ")
        q4 = r.record(source, duration=10)
        text = r.recognize_google(q4)
        print(text)
        for y in text.split():
            if y in hapwrds:
                print("Hm! Let's move on.")
                happy += 1
            elif y in sadwrds:
                print("Interesting. Let's move on.")
                sad += 1
            elif y in angwrds:
                print("Interesting, let's move on")
                angry += 1
            elif y in neutwrds:
                print("Hm, Let's move on.")
                neutral += 1
            elif y in fearwrds:
                print("Interesting. Let's move on.")
                fear += 1
        time.sleep(3)
        print("Next question.")
        time.sleep(1)
        print("You were just emailed by the school telling you that there is school on saturday this week. What is your reaction?\nYou: ")
        q5 = r.record(source, duration=11)
        text = r.recognize_google(q5)
        print(text)
        for k in text.split():
            if k in angwrds:
                if angry <= 1:
                    angry += 1
                    continue
                print("That's understandable, having to go to school on a saturday would make me angry too. Let's move on to the final question")
                angry += 1
            elif k in sadwrds:
                print("I'd feel the same. School is so boring. Let's move on to the final question")
                sad += 1
            elif k in hapwrds:
                print("Happy? I would be really angry. Let's move on to the final question.")
                happy += 1
            elif k in neutwrds:
                print("Oh? Interesting. Let's move on to the final question")
                neutral += 1
            elif k in fearwrds:
                print("Really? That's different. Let's move on to the final question.")
                fear += 1
        time.sleep(3)
        print("Final question!")
        time.sleep(1)
        print("Your friends throw you a surprise party! What is your reaction?\nYou: ")
        q6 = r.record(source, duration=10)
        text = r.recognize_google(q6)
        print(text)
        for z in text.split():
            if z in hapwrds:
                if happy <= 1:
                    happy += 1
                    continue
                print("Me too! I would be so happy.")
                happy += 1
            elif z in sadwrds:
                print("Sad? That's surprising to me. I'm not sure why anyone would feel sad.")
                sad += 1
            elif z in angwrds:
                print("Angry?? That's alarming. ")
                angry += 1
            elif z in neutwrds:
                print("Oh? I guess you're used to surprise parties.")
                neutral += 1
            elif z in fearwrds:
                print("Really? That's different.")
                fear += 1
        def is_duplicate(anylist):
            if type(anylist) != 'list':
                return("Error. Passed parameter is Not a list")
            if len(anylist) != len(set(anylist)):
                return True
            else:
                return False
        time.sleep(3)
        if happy > angry and happy > sad and happy > fear and happy > neutral:
            print("According to my calculations, your mood is happy! :) ")
        elif angry > happy and angry > sad and angry > fear and angry > neutral:
            print("According to my calculations, your mood is angry!! >:( ")
        elif sad > happy and sad > angry and sad > fear and sad > neutral:
            print("According to my calculations, your mood is sad :( ")
        elif fear > happy and fear > angry and fear > sad and fear > neutral:
            print("According to my calculations, your mood is fear! 0_0 ")
        elif neutral > happy and neutral > angry and neutral > sad and neutral > fear:
            print("According to my calculations, your mood is neutral! -_-")
        elif is_duplicate(list):
            print("It seems you have multiple moods! See for yourself.")
            print("happy =", happy)
            print("neutral =", neutral)
            print("angry =", angry)
            print("sad =", sad)
            print("fear =", fear)


        #
        #
        #

        return text
voice()