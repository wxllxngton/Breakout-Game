from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()
        self.goto(position)


    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(y=self.ycor(),x=new_x)


    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(y=self.ycor(),x=new_x)
