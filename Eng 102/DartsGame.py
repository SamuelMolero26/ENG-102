# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   Team Lab 13
# Date:         21 November 2022
#

import turtle
from math import *
import tkinter as tk
import time

#screen size set up

sc = turtle.Screen()
sc.tracer(0)
sc.setup(400, 1000)

rules = turtle.textinput(
  'Rules',
  'You will have 3 attempts to input angle and Velocity (m/s) in order to hit a dart board at a constant distance of 7 feet but with a varying height. You must also enter your own height. Good luck!\nHere are the rules:\n1. The launch angle must be between 0 and 90 degrees.\n2. Your height must be entered in inches.\n*Note: games with sharp objects are not suitable for children\nEnter any letter to continue'
)

shot_cnt = 0 # number of shots made
velocity = None 
angle = None 
height = None 
Player1 = None 
Player2 = None
rounds = 0

def intro():
  if shot_cnt == 0 and rounds <= 3:
      try:
        global angle
        global height
        global Player2
        global Player1
        global velocity
        angle = turtle.numinput("Angle", "Enter lauch Angle")
        velocity = turtle.numinput('Velocity', 'Enter launch Velocity')
        height = turtle.numinput('Height', 'Enter the Height of your person')
        Player1 = turtle.textinput('Player 1', 'Enter your game tag')
        Player2 = turtle.textinput('Player2', 'Enter your game tag')
        if Player2 == Player1:
          raise SyntaxError
      except SyntaxError:
      #while Player1 == Player2:
        Player2 = turtle.textinput('Player2', 'Enter your game tag (must be different than Player 1\'s tag')
  elif shot_cnt >= 3 and rounds <= 3:
      angle = turtle.numinput("Angle", "Enter lauch Angle")
      velocity = turtle.numinput('Velocity', 'Enter launch Velocity')
      height = turtle.numinput('Height', 'Enter the Height of your person')
  elif rounds > 3:
    print("Game Over")
    sc.resetscreen()
    sc.setup(400,800)
    turtle.write("GAME OVER", align = 'center',font=('Arial', 30, 'bold'))
    sc.exitonclick()

     

intro()

score_player1 = 0
score_player2 = 0


#print(angle)
#print(force)
#print(height)
def inm(x):
  x = x * 0.0254
  return x


#Calculations
fiy = velocity * sin(angle)
fix = velocity * cos(angle)
ftime = inm(84) / fix
how_tall = inm(height)
fheight = how_tall + (fiy) * ftime + (.5) * (-9.8) * (ftime**2)


#convert values to turtle stuff
def mtoturtle(x):
  '''Converts a given height to where it would be on graphics'''
  return x / 250


def turtletom(x):
  '''Converts a given graphic spot to what it would be in meters'''
  return x * 250


turheight = mtoturtle(fheight)
print(turheight)

#scoreboard find a random height on the screen and draw board
#stay there for three throws and calculate points
#get new position and be ready for next player
target_dy = 0

c_size = 30

player = 0 # player status

darts = []

sb_color = 'green'
color_latch = False
#creating the board
def draw_scoreboard(draw):
  global score_player1
  global score_player2
  global shot_cnt
  global sb_color
  global color_latch
  ''' draws the score board user score and gametag would be displayed'''
  #draw = turtle.Turtle()
  
  if shot_cnt == 3 and not color_latch:
    sb_color = 'purple' if sb_color == 'green' else 'green'
    color_latch = True

  if shot_cnt != 3:
    color_latch = False

  draw.pencolor(sb_color)
  draw.fillcolor('grey')
  draw.begin_fill()
  draw.speed(50)
  draw.penup()
  draw.hideturtle()
  draw.goto(-175, 320)
  draw.pendown()
  draw.forward(350)
  draw.left(90)
  draw.forward(68)
  draw.left(90)
  draw.forward(350)
  draw.left(90)
  draw.forward(68)
  draw.left(90)
  draw.end_fill()
  draw.penup()
  draw.goto(-173, 390)
  draw.write('Player #1', align='left', font=('Arial', 14, 'bold'))
  draw.goto(173, 390)
  draw.write('Player #2', align='right', font=('Arial', 14, 'bold'))
  draw.goto(-165, 345)
  draw.write(Player1, align='left', font=('Arial', 12, 'bold'))
  draw.goto(164.5, 345)
  draw.write(Player2, align='right', font=('Arial', 12, 'bold'))
  draw.goto(-78, 320)
  draw.pendown()
  draw.goto(-78, 389)
  draw.penup()
  draw.goto(78, 320)
  draw.pendown()
  draw.goto(78, 389)
  draw.penup()
  draw.goto(5.8, 320)
  draw.goto(0, 320)
  draw.pendown()
  draw.goto(0, 389)
  draw.penup()
  draw.goto(-42, 341)
  draw.write(score_player1, align='left', font=('Arial', 16, 'bold'))
  draw.penup()
  draw.goto(42, 341)
  draw.write(score_player2, align='right', font=('Arial', 16, 'bold'))


def game_circle(x, y, r, color, fcolor='black'):
  ball = canvas.create_oval(x - r,
                            y - r,
                            x + r,
                            y + r,
                            fill=fcolor,
                            outline=color,
                            width=50)
  return ball



def drawing_darts(turtle, x, y, color, lenght=c_size):
  ''' draws the dart at the given position'''
  #y += target_dy
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x, y - (lenght / 2))
  turtle.pendown()
  turtle.goto(x, y + (lenght / 2))
  turtle.penup()
  turtle.goto(x - (lenght / 2), y)
  turtle.pendown()
  turtle.goto(x + (lenght / 2), y)
  #print(x, ' ', y)


d = turtle.Turtle(visible=False)
d.color('green')
d.width(4)
d.speed(20)

#--------------------------------------
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('black')
pen.fillcolor('grey')
#point definition/assimgnet and file creation


def point_assignment(d):
  if d <= 10:
    return 100
  elif d <= 40:
    return 75
  elif d <= 60:
    return 50
  elif d <= 100:
    return 25
  else:
    return 0


score_file = open('highest.txt', 'w')  #file to store scores
score_file.write('game tag\tScore\n')


def update_score_file(tag, score):
  global score_player1
  global score_player2

  if tag == Player1:
    score_player1 += score
  else:
    score_player2 += score
  line = '{tag}\t{score}\n'.format(tag=tag, score=score)
  score_file.write(line)
  score_file.flush()


target_y = 0

click_lockout = 10000
def update_dart(x, y):
  global click_lockout
  if click_lockout < 20:
    return
  global shot_cnt
  global player
  global rounds
  if shot_cnt >= 3:
    player = 1 - player
    intro()
    shot_cnt = 0
    rounds += 1 
  shot_cnt += 1

  darts.append((x, y - target_y, 'green' if player == 0 else 'purple'))
  d = sqrt((y - target_y)**2 + (x)**2)
  update_score_file(Player1 if player == 0 else Player2, point_assignment(d))
  click_lockout = 0



canvas = turtle.getcanvas()
parent = canvas.master

def shooting_rec(t):
  t.penup()
  t.goto(-180,-450)
  t.pendown()
  t.pencolor('green')
  t.begin_fill()
  t.forward(350)
  t.left(90)
  t.forward(130)
  t.left(90)
  t.forward(350)
  t.left(90)
  t.forward(130)
  t.left(90)
  t.fillcolor('green')
  t.end_fill()
  t.hideturtle()
  t.penup()
  t.goto(-5,-410)
  t.pencolor('black')
  t.write("Shoot", align = 'center',font=('Arial', 20, 'bold'))
 

if __name__ == '__main__':
  turtle.speed(100)
  move = turtle.Turtle()
  move.speed(0)
  move.width(2)
  move.hideturtle()
  move.penup()
  move.goto(-250, 5)
  move.pendown()
  circles = []
  #circles.append(game_circle(0, 0, 80, 'black', 'black'))
  #circles.append(game_circle(0, 0, 60, 'blue'))
  #circles.append(game_circle(0, 0, 40, 'red'))
  #circles.append(game_circle(0, 0, 10, 'yellow'))
  circles.append((0, 0, 100, 'white'))
  circles.append((0, 0, 80, 'black', 'black'))
  circles.append((0, 0, 60, 'blue'))
  circles.append((0, 0, 40, 'red'))
  circles.append((0, 0, 10, 'yellow'))
  shooting_rec(move)
  sc.onclick(lambda x, y, turtle=d: update_dart(x, turheight))
  sc.onkey(lambda: d.clear(), 'space')

  dt = 0.05
  t = 0

  while True:
    start = time.time()
    turtle.clear()
    draw_scoreboard(turtle)

    target_dy = 60 * sin(2*t)

    target_y = target_dy

    for ball in circles:
      #canvas.move(ball, 0, target_dy/6)
      game_circle(ball[0], ball[1] - target_dy, ball[2], ball[3])
    for dart in darts:
      drawing_darts(turtle, dart[0], dart[1] + target_dy, dart[2])
    sc.update()
    end = time.time()

    if end - start < dt:
      time.sleep(dt)
    t += dt
    click_lockout += 1
    print(click_lockout)
turle.hideturtle()
turtle.done()
