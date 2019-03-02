from turtle import *
speed(9)


def drawBox(sidelength):
    for i in range(4):
        forward(sidelength)
        left(90)


for i in range(36):
    pencolor('blue')
    drawBox(150)
    right(10)

exitonclick()
