from libs.tga_turtle import TGA_Turtle
import math

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
TEST_RATIO = [1, 1, 6]


def turtle_lissajous_curve_circle(tur: TGA_Turtle, params):
    radius = 200
    t1 = TGA_Turtle(is_svg=True, canvas_size=CANVAS_SIZE)
    t2 = TGA_Turtle(is_svg=True, canvas_size=CANVAS_SIZE)

    t1.teleport((0, radius))
    t2.teleport((-radius, 0))
    t1.speed(0)
    t2.speed(0)
    
    for _ in range(360*params[2]):
        t1.circle(radius, extent=params[0])
        t2.circle(radius, extent=params[1])

        tur.goto(t1.pos()[0], t2.pos()[1])


TEST_PARAMS = {
    "iterations": 100,
    "delta1": 0.1,
    "delta2": 0.1,
    "fun1": math.tan,
    "fun2": math.sin
}

def turtle_lissajous_curve_functions(tur: TGA_Turtle, params):
    delta1 = params["delta1"]
    delta2 = params["delta2"]
    fun1 = params["fun1"]
    fun2 = params["fun2"]
    x1 = 0
    x2 = 1
    it = 0

    for _ in range(params["iterations"]):
        if it == 0:
            tur.penup()
        
        tur.goto(fun1(x1)*10, fun2(x2)*100)

        if it == 0:
            tur.pendown()
            it += 1

        x1 += delta1
        x2 += delta2