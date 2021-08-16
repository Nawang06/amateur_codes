from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.make_score()

    def make_score(self, points=0):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=ALIGNMENT)

    def update_score (self):
        self.score += 1
        self.clear()
        self.make_score(self.score)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
