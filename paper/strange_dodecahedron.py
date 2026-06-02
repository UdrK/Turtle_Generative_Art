from art.geometry.strange_dodecahedron import draw_shape
from libs.tga_turtle import TGA_Turtle

## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[1920, 1080])
tur.fillcolor("white")
tur.color("white")
screen = tur.getscreen()
screen.bgcolor("black")

draw_shape(tur, 0, -400, 400)
tur.save_as("../Drawings/strange_dodecahedron.svg")
print("Saved: strange_dodecahedron.svg")