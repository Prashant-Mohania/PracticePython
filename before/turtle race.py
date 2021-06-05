from turtle import Turtle
from random import randint
pramo = Turtle()
pramo.color('red')
pramo.shape('turtle')
pramo.penup()
pramo.goto(-360, 100)
pramo.pendown()


cd = Turtle()
cd.color('green')
cd.shape('turtle')
cd.penup()
cd.goto(-360, 70)
cd.pendown()
for movement in range(350):
    pramo.forward(randint(1, 3))
    cd.forward(randint(1, 3))
