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

    def is_collision(self, other):
        x = self.x - other.x
        y = self.y - other.y
        distance = ((x ** 2) + (y ** 2)) ** 0.5

        if distance <= ((10 * self.size) + (10 * self.size)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "turtle"
        self.lives = 3
        self.score = 0

    def rotate_left(self):
        self.heading += 15

    def rotate_right(self):
        self.heading -= 15

    def accelerate(self):
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx += ax * 0.02
        self.dy += ay * 0.02


player = Player()

sprites = [player]

# keyboard biding
win.listen()
win.onkeypress(player.rotate_left, "a")
win.onkeypress(player.rotate_right, "d")
win.onkeypress(player.accelerate, "w")


# mainloop
while True:
    # update the screen
    win.update()
    pen.clear()

    for sprite in sprites:
        sprite.render(pen)
        sprite.update()

    # collision missile-asteroid

# win.mainloop()
