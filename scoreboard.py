from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 4
        self.update_scoreboard()


    def victory(self, time):
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.update_scoreboard()
        self.clear()
        self.write(arg=f"You Win!\nTime elapsed: {time}s", align=ALIGNMENT, font=FONT)
