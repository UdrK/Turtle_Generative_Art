from svg_turtle import SvgTurtle
from turtle import Turtle
from .turtle_utils import (
    forward_without_drawing,
    forward_optional_draw,
    forward_dashed,
    forward_and_reset,
    without_drawing,
    invariant_draw,
    calculate_circle_center,
    circle_and_return_center,
    circle_centered_at_turtle,
)

class TGA_Turtle:

    def __init__(self, is_svg=False):
        if is_svg:
            self.turtle = SvgTurtle()
        else:
            self.turtle = Turtle()
    
    # region movement

    def forward(self, quantity):
        return self.turtle.forward(quantity)

    def backward(self, quantity):
        return self.turtle.backward(quantity)

    def left(self, angle):
        return self.turtle.left(angle)
    
    def right(self, angle):
        return self.turtle.right(angle)

    def goto(self, *args):
        return self.turtle.goto(*args)

    def setheading(self, angle):
        return self.turtle.setheading(angle)

    # endregion

    # region state

    def position(self):
        return self.turtle.position()

    def pos(self):
        return self.turtle.pos()

    def heading(self):
        return self.turtle.heading()

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()
    
    def towards(self, point):
        return self.turtle.towards(point[0], point[1])

    # endregion

    # region pen control

    def penup(self):
        return self.turtle.penup()
    
    def pendown(self):
        return self.turtle.pendown()
    
    def pensize(self, width=None):
        return self.turtle.pensize(width)
    
    def pencolor(self, *args):
        return self.turtle.pencolor(*args)

    def fillcolor(self, *args):
        return self.turtle.fillcolor(*args)

    def isdown(self):
        return self.turtle.isdown()

    #endregion

    # region drawing

    def dot(self, size=None, color=None):
        return self.turtle.dot(size, color)
    
    def begin_fill(self):
        return self.turtle.begin_fill()
    
    def end_fill(self):
        return self.turtle.end_fill()
    
    def write(self, text, move=False, align="left", font=("Arial", 8, "normal")):
        return self.turtle.write(text, move=move, align=align, font=font)

    # endregion

    # region display

    def hideturtle(self):
        return self.turtle.hideturtle()
    
    def showturtle(self):
        return self.turtle.showturtle()
    
    def speed(self, speed_value):
        return self.turtle.speed(speed_value)

    # endregion

    # region helpers

    def forward_without_drawing(self, distance, heading=None):
        return forward_without_drawing(self.turtle, distance, heading)

    def forward_optional_draw(self, distance, draw=True, heading=None):
        return forward_optional_draw(self.turtle, distance, draw, heading)

    def forward_dashed(self, distance, dash_proportions=(1.25, 1), heading=None):
        return forward_dashed(self.turtle, distance, dash_proportions, heading)

    def forward_and_reset(self, distance, draw=True):
        return forward_and_reset(self.turtle, distance, draw)

    def without_drawing(self, method, keyword_arguments):
        keyword_arguments = dict(keyword_arguments)
        keyword_arguments["tur"] = self.turtle
        return without_drawing(method, keyword_arguments)

    def invariant_draw(self, method, keyword_arguments):
        keyword_arguments = dict(keyword_arguments)
        keyword_arguments["tur"] = self.turtle
        return invariant_draw(method, keyword_arguments)

    def teleport(self, *args):
        return self.turtle.teleport(*args)

    def calculate_circle_center(self, radius):
        return calculate_circle_center(self.turtle, radius)

    def circle_and_return_center(self, radius, extent=None, steps=None):
        return circle_and_return_center(self.turtle, radius, extent, steps)

    def circle_centered_at_turtle(self, radius, extent=None, steps=None):
        return circle_centered_at_turtle(self.turtle, radius, extent, steps)

    # endregion
