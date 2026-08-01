from libs.tga_turtle import TGA_Turtle
from art.geometry import lissajous_curves
from math import sin

## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=lissajous_curves.CANVAS_SIZE)
tur.speed(0)
tur.color("white")
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")

lissajous_curves.turtle_lissajous_curve(tur, lissajous_curves.TEST_RATIO)

filename = "test3.svg"
tur.save_as(f"../Drawings/lissajous_curves/{filename}")
print(f"Saved: {filename}")