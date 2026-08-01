from libs.tga_turtle import TGA_Turtle
from math import sin

CANVAS_SIZE = [1920, 1920]

EYE_RATIO = [1, .99, 15]
DROPLET_RATIO = [1, .99, 30]
PILLOW_RATIO = [1, .89, 30]
PILLOW_2_RATIO = [1, .89, 10]
PILLOW_3_RATIO = [1, .75, 10]
PILLOW_4_RATIO = [1, 1.09, 10]
ES_RATIO = [1, .59, 10]
RIBBON_RATIO = [1, .4, 4]
VORTEX_RATIO = [1, .3, 10]
VORTEX_1_RATIO = [1, .25, 10]
ATOM_1_RATIO = [1, 1.2, 3]
ATOM_2_RATIO = [1, 1.2, 5]
ATOM_3_RATIO = [0.6666666, 1, 4]
FISH_RATIO = [1, 1.49, 10]
BOOMERANG_RATIO = [1, 1.99, 10]
WIDE_BOOMERANG_RATIO = [1, 1.98, 10]
SHELL_RATIO = [1, 1.1, 8]
SHELL2_RATIO = [1, 1.1, 6]
TEST_RATIO = [1, 1.66666, 6]

def turtle_lissajous_curve(tur: TGA_Turtle, ratio):
    radius = 200
    circle_1 = TGA_Turtle(is_svg=True, canvas_size=CANVAS_SIZE)
    circle_2 = TGA_Turtle(is_svg=True, canvas_size=CANVAS_SIZE)

    circle_1.teleport((0, radius))
    circle_2.teleport((-radius, 0))
    circle_1.speed(0)
    circle_2.speed(0)
    
    for _ in range(360*ratio[2]):
        circle_1.circle(radius, extent=ratio[0])
        circle_2.circle(radius, extent=ratio[1])

        tur.goto(circle_1.pos()[0], circle_2.pos()[1])

