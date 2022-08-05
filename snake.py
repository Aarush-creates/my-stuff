print("***** Task 4: *****")
import turtle
import random
def setturtle():
 wn = turtle.Screen()
 # Set the Turtle Screen for the game
 turtle.setup(400,500)
 wn = turtle.Screen() 
 wn.title("Handling keypresses!") 
 wn.bgcolor("lightgreen")

def createsnake():
 turt = turtle.Turtle() 
 turt.shape("arrow")
 turt.color("black")
 turt.penup()
 turt.goto(0,100)
 turt.pensize(7)
 turt.pendown()
 return turt

def createsnakefood():
 food = turtle.Turtle()
 food.speed(0)
 food.shape("circle")
 food.color("red")
 food.penup()
 food.shapesize(0.50, 0.50)
 food.goto(0, 0)
 return food

def randomization():
 z=random.randint(-200,200)
 return z

def turtleup(tess):
  return tess.forward(30)

def turtleleft(tess):
  return tess.left(45)

def turtleright(tess):
  return tess.right(45)

def turtleback(tess):
  return tess.backward(30) 

def turtlequit(tess):
  return tess.hideturtle()
setturtle()
createsnake()
createsnakefood()
def gamerules():
  print("****Rules of the Game****")
  print("The two main characters of this game are:\n- The Snake(Black Arrow)\n- The food(red circle)")
  print("The player has to move the snake such that it eats(touches) the food.")
  print("The players uses the arrow keys to move and turn")
  print("The player gets 10 points if the snake eats the food")
  print("Click the snake(black arrow) and use the arrow keys to start playing")

gamerules()
setturtle()
tess=createsnake()
food=createsnakefood()
# Initialize score

score=0


# Define functions to set snake movement
move_speed = 20
turn_angle = 45
def forward():
  tess.forward(move_speed)
def backward():
  tess.backward(move_speed)
def left():
  tess.left(turn_angle)
def right():
  tess.right(turn_angle) 

# Quit function is done for you. Replace the value in the placeholder

def snakequit():
  tess.hideturtle()
  print("Bye!!")
  print("Click the Stop button to stop the game.")
wn = turtle.Screen()
wn.bgcolor("blue")
#Keyboard binding (code done for you)
while True:
  wn.update()

#  Write code for keyboard binding 
  wn.onkey(forward,"Up")
  wn.onkey(backward,"Down")
  wn.onkey(left,"Left")
  wn.onkey(right,"Right")
  wn.onkey(snakequit, "w")
  wn.listen() 
#Check position of turtle relative to food
  if tess.distance(food)<20 :
    x=randomization()
    y=randomization()
    food.goto(x, y)
    score=score+10
    print("Score: ",score)
wn.mainloop()
