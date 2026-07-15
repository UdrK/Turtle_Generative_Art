from libs.generic_draw import draw
from libs.tga_turtle import TGA_Turtle
import math

def shape(tur:TGA_Turtle, radius):
    tur.setheading(90)
    tur.forward_without_drawing(radius*2)

    B_radius = radius*0.2
    B_A_distance = radius*0.5

    tur.circle_centered_at_turtle(B_radius)
    tur.setheading(270)
    tur.forward_without_drawing(B_radius)
    tur.forward(B_A_distance)
    A_radius = radius*0.3
    tur.forward_without_drawing(A_radius)
    
    A_point = tur.pos()
    tur.circle_centered_at_turtle(A_radius)
    tur.setheading(0)
    tur.forward_without_drawing(A_radius)
    tur.circle(-radius*0.5, 90)

    tur.teleport(A_point)
    tur.setheading(180)
    tur.forward_without_drawing(A_radius)
    tur.circle(radius*0.5, 90)
    
    tur.teleport(A_point)
    tur.setheading(270)
    tur.forward_without_drawing(A_radius)
    tur.forward((radius*1.25)-A_radius)

    C_radius = radius*0.75
    tur.forward_without_drawing(C_radius)
    tur.circle_centered_at_turtle(C_radius)

    tur.setheading(270)
    tur.forward_without_drawing(C_radius)
    tur.forward(C_radius)

    # antennae R

    F_point = tur.pos()
    tur.setheading(0)
    tur.forward(radius*2)

    E_point = tur.pos()

    tur.setheading(120)
    tur.forward_without_drawing(A_radius*3)
    
    D_point = tur.pos()

    tur.forward_without_drawing(A_radius)
    tur.circle_centered_at_turtle(A_radius)

    tur.quadratic_bezier(E_point, [E_point[0], D_point[1]], D_point)

    # antennae L

    tur.teleport(F_point)
    tur.setheading(180)
    tur.forward(radius*2)

    E_point = tur.pos()

    tur.setheading(60)
    tur.forward_without_drawing(A_radius*3)
    
    D_point = tur.pos()

    tur.forward_without_drawing(A_radius)
    tur.circle_centered_at_turtle(A_radius)

    tur.quadratic_bezier(E_point, [E_point[0], D_point[1]], D_point)

    # lower shape

    tur.teleport(F_point)
    tur.setheading(270)
    tur.forward(radius*0.5)

    G_point = tur.pos()

    tur.setheading(0)
    tur.forward_without_drawing(radius*0.75)
    tur.setheading(180)
    tur.forward(radius*1.5)

    tur.teleport(G_point)
    tur.setheading(270)
    tur.forward(radius*2.25)

    H_point = tur.pos()

    tur.forward_without_drawing(A_radius)
    tur.circle_centered_at_turtle(A_radius)

    tur.teleport(H_point)
    tur.setheading(0)
    tur.circle(radius*0.5, 90)

    tur.teleport(H_point)
    tur.setheading(180)
    tur.circle(-radius*0.5, 90)
    


draw_shape_parameters = {"tur": None, 
                        "radius": 150}
draw(shape, draw_shape_parameters, is_svg=True, canvas_size=[1920, 1920])
