import turtle
s = turtle.Screen()
t = turtle.Turtle()

s.getcanvas()
s.canvheight = 100
s.canvwidth = 50
s.bgcolor("black")
s.title("tryouts")
t.circle(10)
t.forward(50)
t.left(60)
t.pencolor("white")
t.penup()
t.goto(0,100)
t.getpen()
t.pencolor("red")

t.pen()
a = 0
b = 0
while True:
    t.forward(50)
    t.left(50)
    t.right(60)
    t.backward(40)
    t.begin_poly()

    if b == 100:
        break


