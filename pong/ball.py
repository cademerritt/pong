from turtle import Turtle

ball = Turtle()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("lightblue")
        self.shape("circle")
        self.u = 20
        self.d = 20

    def ball(self):

        new_u = self.xcor() + self.u
        new_d = self.ycor() + self.d
        self.goto(new_u, new_d)



        # if self.d == 1 and self.u == 1:
        #     xcor = self.xcor() + 20
        #     ycor = self.ycor() + 20
        #
        # elif self.d == 1 and self.u == 0:
        #     xcor = self.xcor() + 20
        #     ycor = self.ycor() - 20
        #     self.goto(xcor, ycor)
        # elif self.d == 0 and self.u == 1:
        #     xcor = self.xcor() - 20
        #     ycor = self.ycor() + 20
        #     self.goto(xcor, ycor)
        # elif self.d == 0 and self.u == 0:
        #     xcor = self.xcor() - 20
        #     ycor = self.ycor() - 20
        #     self.goto(xcor, ycor)

        # if self.ycor() >= 500:
        #     self.u *= 1
        # elif self.ycor() <= -500:
        #     self.u *= -1
        # elif self.distance() < 15 and ball.d == 1:
        #     d = 0
        # else:
        #     pass

    # pad1 = Pad1()


# class Strikes(Pad1):
#
#     def __init__(self, position):
#         super().__init__(position)
# position
# from paddle1 import Pad1
