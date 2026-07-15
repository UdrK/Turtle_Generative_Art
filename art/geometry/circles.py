from libs.generic_draw import draw
from libs.tga_turtle import TGA_Turtle
import math

def get_triangle_vertices(tur, radius):
    center = tur.pos()
    vertices = []

    for i in range(3):
        tur.setheading(30+(120*i))
        tur.forward_without_drawing(radius)
        vertices.append(tur.pos())
        tur.teleport(center)

    return vertices

def draw_triangle(tur, vertices):
    tur.teleport(vertices[0])
    for i in range(3):
        tur.goto(vertices[(i+1)%3])

def draw_lower_reticle(tur, reticle_radius):
    tur.setheading(180)
    tur.forward_without_drawing(reticle_radius)

def draw_reticle(tur, reticle_radius, radius):
    center = tur.pos()

    tur.setheading(180)
    tur.forward_without_drawing(reticle_radius)

    tur.setheading(270)
    tur.circle(reticle_radius, 180, steps=80)

    tur.teleport(center)

    tur.setheading(270)
    tur.forward(radius)

    tur.setheading(90)
    tur.forward_without_drawing(radius+0.5*reticle_radius)
    tur.forward(0.5*reticle_radius)

    point = tur.pos()

    tur.setheading(180)
    tur.circle(reticle_radius, 30, steps=80)

    tur.teleport(point)
    tur.setheading(0)
    tur.circle(-reticle_radius, 30, steps=80)

def draw_small_circles(tur, reticle_radius, small_circles_radius):

    center = tur.pos()

    for i in range(3):
        tur.setheading(90+(120*i))
        tur.forward_without_drawing(reticle_radius+small_circles_radius)
        tur.circle_centered_at_turtle(small_circles_radius, steps=80)
        tur.teleport(center)

def shape(tur: TGA_Turtle, radius):
    tur.circle_centered_at_turtle(radius*1.1, steps=80)
    tur.circle_centered_at_turtle(radius, steps=80)
    tur.circle_centered_at_turtle(radius*0.1, steps=80)

    vertices = get_triangle_vertices(tur, radius*1.1)
    reticle_radius = vertices[0][1]
    small_circles_radius = (radius - reticle_radius)/2 

    tur.invariant_draw(draw_triangle, {"tur": tur, "vertices": vertices})
    tur.invariant_draw(draw_reticle, {"tur": tur, "reticle_radius": reticle_radius, "radius": radius})
    tur.invariant_draw(draw_small_circles, {"tur": tur, "reticle_radius": reticle_radius, "small_circles_radius": small_circles_radius})

draw_shape_parameters = {"tur": None, "radius": 400}
draw(shape, draw_shape_parameters, is_svg=True)