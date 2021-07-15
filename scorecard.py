from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_update()
    def score_update(self):
        self.write(f"Score:{self.score} and High Score :{self.high_score}", align="center", font=("Arial", 24, "normal"))
    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"high score = {int(self.high_score)}")
        self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"game over", align="center", font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()


