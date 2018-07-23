import turtle
turtle.screensize(800,600,"white")
t = turtle.Pen()
t.speed(0)
first = 5
for i in range(9):
    t.up()
    t.goto(0,-20 * i)
    t.down()
    t.circle(20 * i)
    t.up()
t.goto(-20 * 9,-20 * 9)
for i in range(0,4):
    t.down()
    t.forward(360)
    t.left(90)
input()