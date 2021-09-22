from turtle import Turtle

paddle = Turtle()


class Pad1(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pu()
        self.shape("square")
        self.goto(position)
        self.color("white")
        self.shapesize(4, 1)
        self.pu()

    # def paddle1(self):

    # self.setheading(90)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def dw(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

#
# class Pad2(Turtle):
#
#     def __init__(self, posision):
#         super().__init__()
#         self.pu()
#         self.goto(posision)
#
#     def paddle2(self):
#
#         self.color("white")
#         self.shape("square")
#         self.shapesize(0.7, 4)
#         self.setheading(90)
#
#     def up(self):
#         new_y = self.ycor() + 30
#         self.goto(self.xcor(), new_y)
#
#
#     def dw(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)
