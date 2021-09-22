from turtle import Turtle, Screen
from scoreBoard import Score
from paddle1 import Pad1
from ball import Ball
import time

s = Screen()
s.screensize(1850, 1000, "black")
s.setup(1.0, 1.0, None, 0)
t = Turtle()
t.pu()
t.goto(10, 500)
t.color("white")
t.rt(90)
t.shape("square")
t.shapesize(0.7, 2)
sc = Score()
alive = True
sc.si()
sp = 0.1
p1 = Pad1((900, 0))
p2 = Pad1((-900, 0))
b = Ball()
s.listen()
s.onkeypress(p1.up, "Up")
s.onkeypress(p1.dw, "Down")
s.onkeypress(p2.up, "w")
s.onkeypress(p2.dw, "s")
for _ in range(11):
    t.ht()
    t.stamp()
    t.fd(100)
while alive:
    s.update()
    s.tracer(0)
    time.sleep(sp)
    b.ball()
    if b.distance(p1) < 50 and b.xcor() > 860 or b.distance(p2) < 50 and b.xcor() < -860:
        b.u *= -1
        sp *= 0.9
    if b.ycor() >= 500 or b.ycor() <= -500:
        b.d *= -1

    if b.xcor() > 880 or b.xcor() < - 880:
        sc.pt(b.xcor())
        b.goto(0, 0)
        b.u *= -1
        sp = 0.01









s.exitonclick()

# miss

# st = Strikes
# # b.st()
# print(b.d, b.distance(p1))
# if b.distance(p1) <= 25 and b.d == -20:
#     b.d = 20# p2 = Pad2()
# # p1 = Pad1()
# # b.xcor()
# # b.ycor()
# # s.tracer(0)
