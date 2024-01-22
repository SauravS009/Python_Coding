from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_rscore = 0
        self.player2_lscore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.player1_rscore, align="center", font=("arcade", 50, "normal"))
        self.goto(80, 200)
        self.write(self.player2_lscore, align="center", font=("arcade", 50, "normal"))

    def l_update(self):
        self.player2_lscore += 1
        self.update_score()

    def r_update(self):
        self.player1_rscore += 1
        self.update_score()
