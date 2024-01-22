from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        with open("data.txt") as file:
            self.highest_score= int(file.read())
        self.write(f"score:{self.score}   High Score:{self.highest_score}", align="center",
                   font=("Arial", 20, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.highest_score}", align="center", font=("Arial", 20, "normal"))

    def high_score(self):
        if self.score>self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score=0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 20, "normal"))
