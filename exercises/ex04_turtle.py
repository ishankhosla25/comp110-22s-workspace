"""Using Turtle to Draw!"""

__author__ = "730245028"

from turtle import Turtle, colormode, done
colormode(255)
trunk: Turtle = Turtle()
leaves: Turtle = Turtle()


def main() -> None:
    """Entrypoint to Program!"""
    trunk.speed(0)
    leaves.speed(0)
    trunk_width: float = 50
    trunk_height: float = 100
    trunk_x: float = 278
    trunk_y: float = 0
    leaves_width: float = 50
    leaves_x: float = trunk_x + (leaves_width * .5)
    second_leaves_x: float = trunk_x - (leaves_width * .5)
    leaves_y: float = set_leaves_y(trunk_height)
    move: float = 150
    i: int = 0
    while i < 5:
        draw_trunk(trunk, trunk_x, trunk_y, trunk_width, trunk_height)
        draw_leaves(leaves, leaves_x, leaves_y, leaves_width)
        draw_leaves(leaves, second_leaves_x, leaves_y, leaves_width)
        trunk_x -= move
        leaves_x -= move
        second_leaves_x -= move
        i += 1
    i: int = 0
    leaves_y = move_up(leaves_y, leaves_width)
    trunk_x = 278
    while i < 5:
        leaves_x = trunk_x
        draw_leaves(leaves, leaves_x, leaves_y, leaves_width)
        trunk_x -= move
        i += 1
    done()


def set_leaves_y(rectangle_height: float) -> float:
    """Set y startingpoint for leaves!"""
    leaves_y: float = 0
    leaves_y += rectangle_height
    return leaves_y


def move_up(leaves_y: float, leaves_width: float) -> float:
    """Move third leave square up!"""
    leaves_y += leaves_width
    return leaves_y


def draw_trunk(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Drawing the trunk of the tree."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.pencolor("brown")
    a_turtle.fillcolor(145, 97, 25)
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()


def draw_leaves(b_turtle: Turtle, x: float, y: float, width: float) -> None:
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.setheading(0.0)
    b_turtle.pendown()
    b_turtle.begin_fill()
    b_turtle.pencolor("green")
    b_turtle.color(27, 171, 75)
    i: int = 0
    while i < 4:
        b_turtle.forward(width)
        b_turtle.left(90)
        i += 1
    b_turtle.end_fill()


if __name__ == "__main__":
    main()