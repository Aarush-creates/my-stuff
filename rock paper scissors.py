import random
import time
bot = ["rock", "paper", "scissor"]
score = 0
bot_score = 0
while True:
    user = input("Let's play rock, paper, scissors! Pick your option (or type stop to stop game): ")
    randbot = random.choice(bot)
    if user == randbot:
        print("The bot picked: ", randbot)
        print("Tie! Try again.")
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "rock" and randbot == "paper":
        print("The bot picked: ", randbot)
        print("You lose! Try again.")
        bot_score+=1
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "paper" and randbot == "scissor":
        print("The bot picked: ",randbot)
        print("You lose! Try again.")
        bot_score += 1
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "scissor" and randbot == "rock":
        print("The bot picked: ", randbot)
        print("You lose! Try again.")
        bot_score += 1
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "paper" and randbot == "rock":
        print("The bot picked: ", randbot)
        print("You win! Let's go again!")
        score += 1
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "scissor" and randbot == "paper":
        print("The bot picked: ", randbot)
        print("You win! Let's go again!")
        score += 1
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "rock" and randbot == "scissor":
        print("The bot picked: ", randbot)
        print("You win! Let's go again!")
        score += 1
        print("The score is", score, "to", bot_score)
        time.sleep(2)
        continue
    elif user == "stop":
        print("Ok! Thanks for playing!")
        break
    else:
        print("Incorrect value, try again.")
        continue