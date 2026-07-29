from libs.tga_turtle import TGA_Turtle
from libs.geometry_calculations import find_regular_polygon_center

rectangle_width = 191.5
rectangle_height = 130
gap = 12.3

def drawing(tur: TGA_Turtle):
    rectangles_origins = []
    rectangles_origins.append((0 - (gap/2 + rectangle_width), 0 - (gap/2 + rectangle_height)))
    rectangles_origins.append((0 - (gap/2 + rectangle_width), gap/2))
    rectangles_origins.append((gap/2, gap/2))
    rectangles_origins.append((gap/2, 0 - (gap/2 + rectangle_height)))

    for origin in rectangles_origins:
        tur.teleport(origin)
        rectangle(tur)

def rectangle(tur, width=rectangle_width, height=rectangle_height):
    tur.setheading(0)
    tur.forward(width)
    tur.setheading(90)
    tur.forward(height)
    tur.setheading(180)
    tur.forward(width)
    tur.setheading(270)
    tur.forward(height)

## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[420, 297])
tur.color("white")
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")

drawing(tur)

tur.save_as("../Drawings/window.svg")
print("Saved: window.svg")