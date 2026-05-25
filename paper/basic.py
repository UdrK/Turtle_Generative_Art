from geometry.basic import triangle_spiral
from svg_turtle import SvgTurtle

## CANVAS SETUP
tur = SvgTurtle(1920, 1080)
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")
tur.color("white")

triangle_spiral(tur, 300, 20, 119)
tur.save_as("../Drawings/basic_paper.svg")
print("Saved: basic_paper.svg")