from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):

    def __init__(self, move_increment):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.seth(180)
        self.setposition(350, random.randint(-250, 250))
        self.move_increment = move_increment

    def drive(self):
        self.forward(self.move_increment)




