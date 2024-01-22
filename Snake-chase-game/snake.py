from turtle import Turtle

DIST = 20
positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):

        for i in positions:
            self.add_segment(i)

    def add_segment(self, i):
        tom = Turtle(shape='square')
        tom.color("white")
        tom.penup()
        tom.goto(i)
        self.parts.append(tom)

    def extend(self):
        self.add_segment(self.parts[-1].position())

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            x1 = self.parts[i - 1].xcor()
            y1 = self.parts[i - 1].ycor()
            self.parts[i].goto(x1, y1)
        self.head.forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.parts[0].setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.parts[0].setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.parts[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.parts[0].setheading(RIGHT)

    def reset(self):
        for part in self.parts:
            part.goto(1000,1000)
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
