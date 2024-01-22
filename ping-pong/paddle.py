from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(coordinates)

    def up(self):
        self.new_y=self.ycor() + 25
        self.goto(self.xcor(),self.new_y)

    def down(self):
        self.new_y = self.ycor() - 25
        self.goto(self.xcor(), self.new_y)