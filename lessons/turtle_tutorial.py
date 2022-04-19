"""A tutorial on how to use Turtle."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(10)
leo.hideturtle()

colormode(255)
leo.color(99, 204, 250)

leo.penup()
leo.goto(-150, -150)
leo.pendown()

leo.begin_fill()
leo.color("green", "yellow")

i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()
bob.speed(20)
bob.color("black", "black")
bob.penup()
bob.goto(-150, -150)
bob.pendown()
bob.begin_fill()

side_length: float = 300.0
x: int = 0
while x < 50:
    i: int = 0
    while i < 3:
        bob.forward(side_length)
        bob.left(120)
        i += 1
    side_length = side_length * .97
    x += 1

bob.end_fill()

done()