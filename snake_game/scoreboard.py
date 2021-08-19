from turtle import Turtle

with open ("data.txt") as data:
    high = data.read()
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high)
        self.make_score()

    def make_score(self, points=0):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.make_score(self.score)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.make_score()
