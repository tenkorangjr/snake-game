from turtle import Turtle
import random as rand

MINIMUM_WIDTH = -280
MAXIMUM_WIDTH = 280
MINIMUM_HEIGHT = -280
MAXIMUM_HEIGHT = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_position = rand.randint(MINIMUM_WIDTH, MAXIMUM_WIDTH)
        y_position = rand.randint(MINIMUM_HEIGHT, MAXIMUM_HEIGHT)
        self.goto((x_position, y_position))
