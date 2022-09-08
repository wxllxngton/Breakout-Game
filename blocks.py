from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple","magenta","cyan"]

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.all_blocks = []
        y = 250
        x = 350
        for i in range(5):
            color = random.choice(COLORS)
            for j in range(9):
                new_block = Turtle('square')
                new_block.color(color)
                new_block.penup()
                new_block.speed('fastest')
                new_block.shapesize(stretch_len=4,stretch_wid=1)
                new_block.goto(x=x,y=y)
                self.all_blocks.append(new_block)
                if j == 8:
                    y -= 30
                    x = 350
                else:
                    x -= 90


