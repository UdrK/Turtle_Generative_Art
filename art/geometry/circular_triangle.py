from libs.generic_draw import draw
from libs.tga_turtle import TGA_Turtle
import math

def find_outer_triangle_vertices(tur, radius):
    vertices = []
    angle = 360 / 3
    center = tur.pos()

    for i in range(3):
        tur.teleport(center)
        tur.setheading(90+angle*i)
        tur.forward_without_drawing(radius)
        vertices.append(tur.pos())

    return vertices

def draw_triangle(tur, vertices):
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

def find_inner_triangle_edges(tur, radius):
    center = tur.pos()
    angle = 360 / 3
    edges = []

    for i in range(3):
        tur.teleport(center)
        tur.setheading(30+angle*i)
        tur.forward_without_drawing(radius)
        edges.append(tur.pos())

    return edges

def find_inner_triangle_vertices(tur, radius):
    def find_hypotenuse(radius):
        return abs(radius / math.cos(math.radians(120)))

    return find_outer_triangle_vertices(tur, find_hypotenuse(radius))

def draw_inner_triangle(tur, vertices, edges, radius):

    def find_intersecting_point(tur, radius, multi=1):
        tur.teleport(center)
        tur.setheading(66.66+multi*120)
        point = tur.forward_without_drawing(radius)
        tur.teleport(center)
        return point

    center = tur.pos()

    indices = [(0, 2), (1, 0), (2, 1)]
    for c in indices:
        tur.teleport(edges[c[0]])
        tur.goto(vertices[c[1]])
    
    for i in range(3):
        intersecting_point = find_intersecting_point(tur, radius, i)
        tur.teleport(vertices[i])
        tur.goto(intersecting_point)

def draw_outer_inner_circle(tur, radius):
    arc_degree_extension = (90+23.333)-30

    center = tur.pos()
    angle = 360 / 3

    for i in range(3):
        tur.setheading(30+angle*i)
        tur.forward_without_drawing(radius)
        tur.setheading(angle*((i+1)%3))
        tur.circle(radius, arc_degree_extension, steps=80)
        tur.teleport(center)

def shape(tur, radius):
    tur.circle_centered_at_turtle(radius*1.1, steps=80)
    tur.circle_centered_at_turtle(radius, steps=80)
    tur.circle_centered_at_turtle(radius*0.4, steps=80)
    tur.circle_centered_at_turtle(radius*0.075, steps=80)

    params = { "tur": tur, "radius": radius }
    inner_triangle_params = { "tur": tur, "radius": radius*0.4 }
    outer_vertices = tur.invariant_draw(find_outer_triangle_vertices, params)
    inner_vertices = tur.invariant_draw(find_inner_triangle_vertices, inner_triangle_params)
    inner_edges = tur.invariant_draw(find_inner_triangle_edges, inner_triangle_params)

    outer_triangle_parameters = { "tur": tur, "vertices": outer_vertices}
    inner_triangle_parameters = { "tur": tur, "vertices": inner_vertices, "edges": inner_edges, "radius": radius*0.5}
    outer_inner_circle_params = { "tur": tur, "radius": radius*0.5 }
    tur.invariant_draw(draw_triangle, outer_triangle_parameters)
    tur.invariant_draw(draw_inner_triangle, inner_triangle_parameters)
    tur.invariant_draw(circles, params)
    tur.invariant_draw(draw_outer_inner_circle, outer_inner_circle_params)

draw_shape_parameters = {"tur": None, 
                        "radius": 300}
draw(shape, draw_shape_parameters, True)
