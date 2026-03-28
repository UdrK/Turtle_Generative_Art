import colorsys as cs
from numpy import interp

cool_gray = "#708090"
random_col = ["#009698", "#0047ab", "#a74d0f", "#708090", "#ggd700", "#ff7373", "#20b2aa"]
color_pal = ["#780000", "#c1121f", "#fdf0d5", "#003049", "#669bbc"]
colors = color_pal

def smooth_color(max, current):
            rgb = hsv2rgb(interp((current)%max,[0, max],[0.2,0.8]), 0.75, 0.45)
            return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def regular_polygon(tur, size, sides):
    angles = 360/sides
    for _ in range(sides):
        tur.forward(size)
        tur.right(angles)

def polygon_loop(tur, poly_size, poly_sides):
    while True:
        regular_polygon(tur, poly_size, poly_sides)
        tur.right(5)
        if tur.heading() == 0:
            break

def dialable_polygon_loop(tur, poly_size, poly_sides, poly_num):
    angle = 360/poly_num
    for i in range(poly_num):
        regular_polygon(tur, poly_size, poly_sides)
        tur.right(angle)

def concentric_loops(tur):
    polygon_loop(tur, 100, 3)
    polygon_loop(tur, 100, 4)
    polygon_loop(tur, 100, 5)

def move_circle(tur, size=200):
    tur.penup()
    tur.forward(size)
    tur.right(size)
    tur.pendown()

def turtle_piloted_loop(tur, pilot_tur, loop_c, pilot_move):
    for i in range(loop_c):
        pilot_move(pilot_tur)
        tur.penup()
        tur.goto(pilot_tur.pos())
        tur.pendown()
        sides = 3
        # if i % 3 == 1:
        #     sides = 4
        polygon_loop(tur, 100, sides)


def spiral_polygon(tur, sides, loops):
    for i in range(loops):
        # tur.color(smooth_color(loops, i))
        # tur.color(colors[i%sides])
        tur.forward(i*2)
        tur.right((360/sides)+1)

def tree(tur, size, angle, recursion_depth):
    if recursion_depth > 0:
        tur.forward(size)
        tur.right(angle)

        tree(tur, 0.8*size, angle, recursion_depth-1)

        tur.left(2*angle)

        tree(tur, 0.5*size, angle, recursion_depth-1)

        tur.right(angle)
        tur.forward(-size)

def rec_poly(tur, size, sides, level, multi):
    if level > 0:
        for i in range(sides):
            rec_poly(tur, multi*size, sides, level-1, multi)
            tur.forward(size)
            tur.right(360/sides)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in cs.hsv_to_rgb(h,s,v))

def triangle_spiral(tur, step, length, angle):
    for i in range(0, step):
        for b in range(0, 2):
            tur.color(smooth_color(step, i))
            tur.forward(length+i*2)
            tur.right(angle+(b/2))