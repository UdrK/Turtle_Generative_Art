from libs.tga_turtle import TGA_Turtle
from libs.geometry_calculations import find_circle_center_passing_through_two_points

screen_width = 1920
screen_height = 1080
## CANVAS SETUP
tur = TGA_Turtle(is_svg=False, canvas_size=[screen_width, screen_height])
tur.color("white")
tur.speed(0)
tur.hideturtle()
screen = tur.getscreen()
screen.bgcolor("black")

def flower(tur: TGA_Turtle, radius):
    center = tur.pos()
    inner_circle_radius = radius*0.25

    tur.circle_centered_at_turtle(radius)
    first_polygon_vertices = tur.polygon_centered_at_turtle(radius, 5, 90)
    second_polygon_vertices = tur.polygon_centered_at_turtle(radius, 5, 90+((360/5)/2), True)
    tur.setheading(90)
    tur.forward(radius)
    tur.teleport(center)
    tur.circle_centered_at_turtle(inner_circle_radius)

    inner_circle_vertices = []

    for i in range(len(second_polygon_vertices)):
        tur.teleport(center)
        tur.setheading(tur.towards(second_polygon_vertices[i]))
        tur.forward(inner_circle_radius)
        inner_circle_vertices.append(tur.pos())

    petal_circle_radius = inner_circle_radius*0.75

    circle_centers = []
    for i in range(len(inner_circle_vertices)):
        center = find_circle_center_passing_through_two_points(inner_circle_vertices[i], inner_circle_vertices[(i+1)%len(inner_circle_vertices)], petal_circle_radius)
        circle_centers.append(center[1])
        tur.teleport(center[1])
        tur.circle_centered_at_turtle(petal_circle_radius)

    petals_outer_circle_vertices = [first_polygon_vertices[0], first_polygon_vertices[1], first_polygon_vertices[2]]
    petals_inner_circle_vertices = [inner_circle_vertices[0], inner_circle_vertices[1], inner_circle_vertices[2]]
    petal_circle_centers = [circle_centers[0], circle_centers[1], circle_centers[4]]

    tur.pensize(2)
    tur.color("purple")

    # petal 1

    tur.teleport(petals_inner_circle_vertices[0])
    tur.setheading(tur.towards(petal_circle_centers[2])-90)
    tur.circle(petal_circle_radius, extent=-45)

    aux = tur.pos()
    tur.dot()
    tur.write("a")

    bez_point_1 = (0, 225)
    bez_point_2 = (-50, 180)

    tur.teleport(bez_point_1)
    tur.dot()
    tur.write("1")
    
    tur.teleport(bez_point_2)
    tur.dot()
    tur.write("2")
    tur.teleport(aux)

    tur.cubic_bezier(tur.pos(), bez_point_2, bez_point_1, petals_outer_circle_vertices[0])

    # petal 2

    tur.teleport(petals_base_points[0])
    tur.setheading(tur.towards(petal_aux_circle_centers[0])-90)
    tur.circle(petal_circle_radius, extent=45)
    print(tur.pos())
    print(petals_vertices[1])

    aux = tur.pos()
    tur.dot()
    tur.write("a")

    tur.right(start_bez_point_angle)
    tur.forward_without_drawing(distance_between_two_points(bezier_triangle[0],  bezier_triangle[1]))
    bez_point_2 = tur.pos()

    tur.teleport(drawing_center)
    tur.setheading(tur.towards(petals_vertices[1]))
    tur.forward_without_drawing(radius*0.75)
    bez_point_1 = tur.pos()

    tur.teleport(bez_point_1)
    tur.dot()
    tur.write("1")
    
    tur.teleport(bez_point_2)
    tur.dot()
    tur.write("2")
    tur.teleport(aux)

    tur.cubic_bezier(tur.pos(), bez_point_2, bez_point_1, petals_vertices[1])


flower(tur, 300)

screen.mainloop()
#tur.save_as("../flower.svg")