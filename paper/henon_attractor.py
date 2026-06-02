from libs.tga_turtle import TGA_Turtle
from art.strange_attractors.henon_attractor import loop

screen_width = 1920
screen_height = 1080
## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[screen_width, screen_height])
tur.color("white")
tur.penup()
screen = tur.getscreen()
screen.bgcolor("black")

x0 = 0.01
y0 = 0.01
for i in range(50):
    term = i*0.01
    loop(tur, x0+term, y0+term, screen_width, screen_height)

tur.save_as("../Drawings/henon.svg")