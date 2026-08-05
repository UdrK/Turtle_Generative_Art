from libs.tga_turtle import TGA_Turtle
from libs.geometry_calculations import find_circle_center_passing_through_two_points
from art.geometry.penta_flower import flower

screen_width = 1920
screen_height = 1080
## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[screen_width, screen_height])
tur.color("white")
tur.speed(0)
tur.hideturtle()
screen = tur.getscreen()
screen.bgcolor("black")

flower(tur, 300)

screen.mainloop()
tur.save_as("../Drawings/penta_flower.svg")