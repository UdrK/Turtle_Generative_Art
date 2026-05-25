from geometry.l_system import draw_algae_l_system, calculate_l_system, algae
from libs.tga_turtle import TGA_Turtle

## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[1440, 2440])
inner = tur.turtle
inner.fillcolor("white")
screen = inner.getscreen()
screen.bgcolor("black")
inner.color("white")

rules = algae()
lsystem = calculate_l_system(rules["iterations"], rules["axiom"], rules["rules"])

tur.setheading(90)
tur.teleport([-500, -800])

draw_algae_l_system(tur, lsystem, rules["angle"], rules["length"])
tur.save_as("../Drawings/algae_l_system.svg")
print("Saved: algae_l_system.svg")
