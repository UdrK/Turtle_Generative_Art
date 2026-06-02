from art.geometry.circles_and_triangles import draw_shape
from libs.tga_turtle import TGA_Turtle

## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[1920, 1080])
tur.fillcolor("white")
tur.color("white")
screen = tur.getscreen()
screen.bgcolor("black")

draw_shape(tur)
tur.save_as("../Drawings/circles_and_triangles.svg")
print("Saved: circles_and_triangles.svg")