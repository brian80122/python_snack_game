import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('orange')
        self.speed('fastest')

        self.set_position()

    def set_position(self):
        self.setx(random.randint(-280, 280))
        self.sety(random.randint(-280, 280))
