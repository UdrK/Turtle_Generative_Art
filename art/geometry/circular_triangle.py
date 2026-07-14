from libs.generic_draw import draw
from libs.tga_turtle import TGA_Turtle

def find_outer_triangle_vertices(tur: TGA_Turtle, radius):
    vertices = []
    angle = 360 / 3
    center = tur.pos()

    for i in range(3):
        tur.teleport(center)
        tur.setheading(90+angle*i)
        tur.forward_without_drawing(radius)
        vertices.append(tur.pos())

    return vertices

def draw_triangle(tur: TGA_Turtle, vertices):
    tur.teleport(vertices[-1])
    for vertex in vertices:
        tur.goto(vertex)

def circles(tur, radius):
    angle = 360 / 3
    center = tur.pos()

    for i in range(3):
        tur.teleport(center)
        tur.setheading(30+angle*i)
        tur.forward_without_drawing(radius*0.8)
        tur.circle_centered_at_turtle(radius*0.075, steps=80)

def shape(tur: TGA_Turtle, radius):
    tur.circle_centered_at_turtle(radius*1.1, steps=80)
    tur.circle_centered_at_turtle(radius, steps=80)
    tur.circle_centered_at_turtle(radius*0.4, steps=80)
    tur.circle_centered_at_turtle(radius*0.5, steps=80)
    tur.circle_centered_at_turtle(radius*0.075, steps=80)

    params = { "tur": tur, "radius": radius }
    vertices = tur.invariant_draw(find_outer_triangle_vertices, params)

    triangle_parameters = { "tur": tur, "vertices": vertices} 
    tur.invariant_draw(draw_triangle, triangle_parameters)
    tur.invariant_draw(circles, params)


draw_shape_parameters = {"tur": None, 
                        "radius": 300}
draw(shape, draw_shape_parameters, True)
