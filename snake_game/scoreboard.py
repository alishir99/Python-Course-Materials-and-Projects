
from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Arial", 8, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        with open ("../../Desktop/data.txt") as data:
           self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.write(f"score:{self.score}  high score: {self.high_score}", align=ALIGNEMENT, font=FONT)

    def inc_score(self):
        self.score +=1
        self.update()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../Desktop/data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score =0
        self.update()


