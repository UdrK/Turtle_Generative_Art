from geometry.l_system import draw_algae_l_system, calculate_l_system, algae
from libs.turtle_utils import teleport
from svg_turtle import SvgTurtle


## CANVAS SETUP
tur = SvgTurtle(1440, 2440)
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")
tur.color("white")

rules = algae()
lsystem = calculate_l_system(rules["iterations"], rules["axiom"], rules["rules"])

tur.setheading(90)
teleport(tur, [-500, -800])

draw_algae_l_system(tur, lsystem, rules["angle"], rules["length"])
tur.save_as("../Drawings/algae_l_system.svg")
print("Saved: algae_l_system.svg")