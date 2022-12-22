import turtle
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Arena!")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Game():
    def __init__(self,width,height):
        self.width = width
        self.height = height


    def render_border(self,pen):
        pen.color("white")
        pen.width(3)
        pen.penup()

        left = -self.width/2.0
        right = self.width/2.0
        top = self.height/2.0
        bottom = -self.height/2.0

        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

class Sprite():
    # Constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.003
        self.health = 100
        self.max_health = 100
        self.width = 20
        self.height = 20

    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False
        
    def update(self):
        self.heading += self.da
        self.heading %= 360
        
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
        self.x += self.dx
        self.y += self.dy

        self.border_check()
        
    def border_check(self):
        if self.x > game.width/2.0 - 10:
            self.x = game.width/2.0 - 10
            self.dx *= -1

        elif self.x <- game.width/2.0 + 10:
            self.x = -game.width/2.0 + 10
            self.dx *= -1

        elif self.y > game.height/2.0 - 10:
            self.y = game.height/2.0 - 10
            self.dy *= -1

        elif self.y <- game.height/2.0 + 10:
            self.y = -game.height/2.0 + 10
            self.dy *= -1

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        
        self.render_health_meter(pen)
        
    def render_health_meter(self, pen):
        # Draw health meter
        pen.goto(self.x - 10, self.y + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)
        
        if self.health/self.max_health < 0.3:
            pen.color("red")
        elif self.health/self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20.0 * (self.health/self.max_health))
        
        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health-self.health)/self.max_health))
        
        pen.penup()
        
class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0
        
    def rotate_left(self):
        self.da = 5
        
    def rotate_right(self):
        self.da = -5
        
    def stop_rotation(self):
        self.da = 0
        
    def accelerate(self):
        self.thrust += self.acceleration
        
    def decelerate(self):
        self.thrust = 0.0

    def fire(self):
        missile.fire(self.x, self.y, self.heading, self.dx, self.dy)
        
    def render(self, pen):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        
        pen.shapesize(1.0, 1.0, None)
        
        self.render_health_meter(pen)

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.state = "ready"
        self.fuel = 100
        self.thrust = 1.0
        self.max_fuel = 200
        self.fuel =self.max_fuel
        self.height = 4
        self.width = 4

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready" :
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy

            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <=0:
                self.reset()
   
            self.heading += self.da
            self.heading %= 360
                  
            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    def render(self, pen):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
        
            pen.shapesize(1.0, 1.0, None)


class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        
#create game object
game=Game(1000, 300)

# Create player sprite
player = Player(0, 0, "triangle", "white")


#create missil object
missile = Missile(0, 100, "circle", "yellow")

enemy = Enemy(0, 100, "square", "red")
enemy.dx = -0.1
enemy.dy = -0.03

enemy2 = Enemy(-100, 100, "square", "red")
enemy2.dx = 0.1
enemy2.dy = 0.03

powerup = Powerup(0, -100, "circle", "blue")
powerup.dy = 0.1
powerup.dx = 0.01

powerup2 = Powerup(-100, -100, "circle", "blue")
powerup2.dy = -0.1
powerup2.dx = -0.01

# Sprites list
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)
sprites.append(missile)
sprites.append(enemy2)
sprites.append(powerup2)

# Keyboard bindings
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")

wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")

wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")

wn.onkeypress(player.fire, "space")

# Main Loop
while True:
    # Clear screen
    pen.clear()
    
    # Do game stuff
    # Update sprites
    for sprite in sprites:
        sprite.update()

    #check for collisions
    for sprite in sprites:
        if isinstance(sprite ,Enemy):
            if player.is_collision(sprite):
                player.x = 0
                player.y = 0

            if missile.state == "active" and missile.is_collision(sprite):
                sprite.x = -100
                sprite.y = -100
                missile.reset()

        if isinstance(sprite, Powerup):
            if player.is_collision(sprite):
                sprite.x = 100
                sprite.y = 100

            if missile.state == "active" and missile.is_collision(sprite):
                sprite.x = +100
                sprite.y = +100
                missile.reset()

    # Render sprites
    for sprite in sprites:
        sprite.render(pen)

    game.render_border(pen)
        
    # Update the screen
    wn.update()
