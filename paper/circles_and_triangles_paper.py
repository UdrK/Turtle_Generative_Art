from geometry.circles_and_triangles import draw_shape
from svg_turtle import SvgTurtle

## CANVAS SETUP
tur = SvgTurtle(1920, 1080)
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")
tur.color("white")

draw_shape_parameters = {"tur": tur}
draw_shape(tur)
tur.save_as("../Drawings/circles_and_triangles.svg")
print("Saved: basic_paper.svg")