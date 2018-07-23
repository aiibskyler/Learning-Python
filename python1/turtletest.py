import turtle
#turtle.screensize(800,600,"white")
t = turtle.Pen()
first = 5
second = 5
t.speed(0)
t.left(90)
t.forward(first)
for i in range(0,100):
    t.left(90)
    t.forward(second)
    second+=4
    first += 4
    t.left(90)
    t.forward(first)
input()