#SNAKE GAME

#GAME
#IMPORT MODULES
import turtle
import time
import random
import mysql.connector

def savescore(v1):
    mydb=mysql.connector.connect(host="localhost",user="root",password="tewani",database="school")

    mycursor=mydb.cursor()
    u11="update players set score="
    v11=" where name='HARSH'"
    sql=u11+v1+v11
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
#Time Delay
delay = 0.075

#Score
score=0
high_score=0

#set up screen
window=turtle.Screen()

#Title
window.title("SNAKE GAME")

#Color Background
window.bgcolor("blue")

#Size of SCreen
window.setup(width=700, height= 700)

#tracer details
window.tracer(0) #TURNS OFFSCREEN UPDATES

#Snake Head
head= turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Functions
    #Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x + 20)

#Snake Food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Segments
segments = []

#PEN
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score : 0  High Score : 0", align="center", font=("Courier", 24, "normal"))

#Key Movements
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

#MAIN GAME LOOP
while True:
    window.update()
    #collision with border
    if head.xcor()>340 or head.xcor()<-340 or head.ycor()>340 or head.ycor()<-340:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #hide segment after collision
        for segment in segments:
            segment.goto(1000,1000)
        #clear the segment lists
        segments.clear()

        #Reset the score
        score=0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 30, "normal"))

    if head.distance(food) < 20:
        # Move food to random
        x=random.randint(-330, 330)
        y=random.randint(-330, 330)
        food.goto(x,y)

        #add segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)



        #increase score
        score+=10
        if score>high_score:
            high_score=score
            savescore(str(high_score))
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align= "center", font=("courier",30,"normal"))

    #move the end segment first
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #check for head and body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #hide the segments
            for segment in segments :
                segment.goto(1000,1000)
                # clear the segment lists
            segments.clear()

            # Reset the score
            score = 0

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("courier", 30, "normal"))


            segments.clear()

    time.sleep(delay)



window.mainloop()






