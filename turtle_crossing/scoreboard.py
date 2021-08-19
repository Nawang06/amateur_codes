from turtle import  Turtle
FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.make_score()

    def make_score(self):
        self.hideturtle()
        self.penup()
        self.goto(-240, 240)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.make_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font=FONT)