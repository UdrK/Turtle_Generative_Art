import turtle
from svg_turtle import SvgTurtle
from geometry.penrose_kite import penrose_kite, long_side

# simple turtle setup method used in the methods below for drawing
def setup_turtle(save_as_svg=True):
    if save_as_svg:
        tur = SvgTurtle(1920, 1080) 
        tur.pensize(0.25)
        screen = tur.getscreen()
        screen.bgcolor("white")
        tur.color("black")
    else:
        tur = turtle.Turtle()
        screen = turtle.Screen()
        screen.bgcolor("white")
        tur.color("black")
    return tur

# method that uses the turtle to draw one Penrose kite
def draw_penrose_kite_to_svg(filename, size=200, recursion_level=8):
    save_as_svg = True
    tur = setup_turtle(save_as_svg)

    # turning turtle on its side
    tur.setheading(-54)

    penrose_kite(tur, size, long_side(size), recursion_level)

    if save_as_svg:
        tur.save_as(filename)
    else:
        tur.getscreen().mainloop()

# method that uses the turtle to draw one Penrose kite in a decagon
# the decagon is made of 5 Penrose kites, each rotated by 72 degrees
def draw_penrose_kite_to_svg_decagon(filename, size=200, recursion_level=8):
    save_as_svg = True
    tur = setup_turtle(save_as_svg)

    for i in range(5):
        tur.setheading((i*72)-18) # 18 degrees align the decagon with the screen
        penrose_kite(tur, size, long_side(size), recursion_level)

    if save_as_svg:
        tur.save_as(filename)
    else:
        tur.getscreen().mainloop()
    
draw_penrose_kite_to_svg("../Drawings/penrose_kite_9.svg", size=200, recursion_level=8)