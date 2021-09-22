from turtle import Turtle

ALIGN = "CENTER"
FONT = ("Arial", 60, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.score1 = 0
        self.score2 = 0
        self.goto(0, 450)

    def si(self):
        self.clear()
        self.ht()
        self.write(f"{self.score1}      {self.score2}", align=ALIGN, font=FONT)




    def pt(self, p):
        if p < 0:
            self.score2 += 1
        else:
            self.score1 += 1
        self.si()

