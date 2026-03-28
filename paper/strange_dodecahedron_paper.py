from geometry.strange_dodecahedron import draw_shape
from svg_turtle import SvgTurtle

## CANVAS SETUP
tur = SvgTurtle(1920, 1080)
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")
tur.color("white")

draw_shape(tur, 0, -400, 400)
tur.save_as("../Drawings/strange_dodecahedron.svg")
print("Saved: strange_dodecahedron.svg")