import turtle
import math

WIDTH = 800
HEIGHT = 600

win = turtle.Screen()
win.bgcolor("black")
win.title("Asteroids")
win.setup(WIDTH, HEIGHT)
win.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)

asteroids = []
missiles = []


class Sprite:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        self.active = True

    def render(self, pen_):
        if self.active:
            pen_.setheading(self.heading)
            pen_.penup()
            pen_.speed(0)
            pen_.goto(self.x, self.y)
            pen_.shape(self.shape)
            pen_.color(self.color)
            pen.shapesize(self.size, self.size, 0)

            pen_.stamp()

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # keep sprite wrapping around screen
        if self.x > WIDTH / 2:
            self.x = (WIDTH / 2) * -1
        elif self.x < (WIDTH / 2) * -1:
            self.x = WIDTH / 2

        if self.y > HEIGHT / 2:
            self.y = (HEIGHT / 2) * -1
        elif self.y < (HEIGHT / 2) * -1:
            self.y = HEIGHT / 2

    @staticmethod
    def is_collision(one, other):
        x = one.x - other.x
        y = one.y - other.y
        distance = ((x ** 2) + (y ** 2)) ** 0.5

        if distance <= ((10 * one.size) + (10 * one.size)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "turtle"

    def rotate_left(self):
        self.heading += 15

    def rotate_right(self):
        self.heading -= 15

    def accelerate(self):
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx += ax * 0.02
        self.dy += ay * 0.02


class Asteroid(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self.shape = "circle"
        self.color = "grey"
        self.x = 100
        self.y = 100


class Missile(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self.shape = "circle"
        self.color = "red"
        self.size = 0.2
        self.active = False

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # keep sprite wrapping around screen
        if self.x > WIDTH / 2:
            self.active = False
        elif self.x < (WIDTH / 2) * -1:
            self.active = False

        if self.y > HEIGHT / 2:
            self.active = False
        elif self.y < (HEIGHT / 2) * -1:
            self.active = False

    def fire(self):
        if not self.active:
            self.active = True
            missiles.append(self)
            self.x = player.x
            self.y = player.y
            self.heading = player.heading
            self.dx += math.cos(math.radians(self.heading)) * 2
            self.dy += math.sin(math.radians(self.heading)) * 2


player = Player()

asteroid = Asteroid()
asteroid.dx = 0.1
asteroid.dy = 0.1

missile = Missile()

# keyboard biding
win.listen()
win.onkeypress(player.rotate_left, "a")
win.onkeypress(player.rotate_right, "d")
win.onkeypress(player.accelerate, "w")
win.onkeypress(missile.fire, "space")

# mainloop
while True:
    # update the screen
    win.update()
    pen.clear()

    player.render(pen)
    player.update()

    missile.render(pen)
    missile.update()

    asteroid.render(pen)
    asteroid.update()

    # collision missile-asteroid
    # if Sprite.is_collision(missile, asteroid):

# win.mainloop()
