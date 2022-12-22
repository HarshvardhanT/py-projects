#space game
import turtle
import os
import math
import random

#set up a screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("bg.gif")

#register the shape
turtle.register_shape("pl1.gif")
turtle.register_shape("invader.gif")

#Draw Border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score=0

#Draw score
score_pen =turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring="Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("green")
player.shape("pl1.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed = 15

#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x< -280:
        x=-280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x>280:
        x=280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate="fire"
        #move the bullet just above the player
        x=player.xcor()
        y=player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#choose the no. of enemies
number_of_enemies = 5
#Create an enemy list
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

#Creating enemy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)
enemyspeed=2

#Creating the Player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready- ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Creating keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main Game loop
while True:
    for enemy in enemies:
        #moving enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        
        #enemy boundary
        if enemy.xcor()>280:

            #moves all the enemiis down
            for e in enemies:
                y= e.ycor()
                y-=40
                e.sety(y)
            #Change enemy direction    
            enemyspeed *=-1

        if enemy.xcor()<-280:
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *=-1

        #collision between bullet and enemy
        if isCollision(bullet, enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,250)
            enemy.setposition(x,y)
            #update score
            score +=10
            scorestring="Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            breakpoint
    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y +=bulletspeed
        bullet.sety(y)

    #Check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate="ready"
    
delay = raw_input("Press Enter to Finish.")
