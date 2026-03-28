import turtle
import svg_turtle
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from libs.geometry_calculations import distance_between_two_points, find_regular_polygon_center
from libs.turtle_utils import forward_without_drawing
from libs.utils import label_points, label_point

# source: /home/kappa/Pictures/sep25sq.gif

def draw_circle(tur, x, y, radius):
    def calculate_circle_center(x, y, radius):
        return x, y+radius

    tur.teleport(x, y)
    tur.circle(radius)

    return calculate_circle_center(x, y, radius)

def draw_big_triangles(tur, circle_center, radius):
    def calculate_triangles_vertices(tur, circle_center, radius):
        tur.penup()
        triangle_vertices = []
        starting_angle = 30
        x, y = circle_center
        for i in range(0, 6):
            angle = starting_angle + i * 60
            tur.teleport(x, y)
            tur.setheading(angle)
            tur.forward(radius)
            triangle_vertices.append([tur.position()[0], tur.position()[1]])
        tur.pendown()
        return triangle_vertices

    def draw_triangles(tur, triangles_vertices):
        i = 0
        for vertex in triangles_vertices:
            tur.teleport(vertex[0], vertex[1])
            tur.goto(triangles_vertices[(i+2)%len(triangles_vertices)])
            i+=1

    triangles_vertices = calculate_triangles_vertices(tur, circle_center, radius)
    draw_triangles(tur, triangles_vertices)
    return triangles_vertices

def find_hexagon_half_point(tur, circle_center, vertex):
    def position_turtle_at_center_towards_vertex(tur, circle_center, vertex):
        tur.teleport(circle_center[0], circle_center[1])    
        vertex_heading = tur.towards(vertex[0], vertex[1])
        tur.setheading(vertex_heading)

    def find_point_by_turtle(tur, distance_to_point):
        forward_without_drawing(tur, distance_to_point)
        return [tur.pos()[0], tur.pos()[1]]

    position_turtle_at_center_towards_vertex(tur, circle_center, vertex)
    center_vertex_half_distance = distance_between_two_points(circle_center, vertex) / 2
    return find_point_by_turtle(tur, center_vertex_half_distance)

def draw_small_outer_triangles(tur, circle_center, big_triangles_vertices, big_triangle_side_length):
    def find_small_side_length(big_triangle_side_length):
        big_side = big_triangle_side_length / 3
        twice_small_side = big_side * 5 / 8
        small_side = twice_small_side / 2
        return small_side
    
    def find_vertex_heading(tur, center, vertex):
        tur.teleport(center[0], center[1])
        return tur.towards(vertex[0], vertex[1])

    def find_small_sides_vertices_from_turtle(tur, hexagon_half_point, vertex_heading, small_side_length):
        tur.teleport(hexagon_half_point[0], hexagon_half_point[1])
        small_side_first_vertex = forward_without_drawing(tur, small_side_length, vertex_heading+90)
        small_side_second_vertex = forward_without_drawing(tur, -2*small_side_length, vertex_heading+90)
        return [small_side_first_vertex, small_side_second_vertex]

    def draw_from_triangle_point_to_vertex(tur, triangle_point, vertex):
        tur.teleport(triangle_point[0], triangle_point[1])
        tur.goto(vertex)

    small_sides_vertices = []
    small_side_length = find_small_side_length(big_triangle_side_length)
    for vertex in big_triangles_vertices:
        vertex_heading = find_vertex_heading(tur, circle_center, vertex)
        hexagon_half_point = find_hexagon_half_point(tur, circle_center, vertex)
        small_sides_vertices_for_vertex = find_small_sides_vertices_from_turtle(tur, hexagon_half_point, vertex_heading, small_side_length)
        draw_from_triangle_point_to_vertex(tur, hexagon_half_point, vertex)
        for small_sides_vertex in small_sides_vertices_for_vertex:
            draw_from_triangle_point_to_vertex(tur, small_sides_vertex, vertex)

        small_sides_vertices.append(small_sides_vertices_for_vertex[0])
        small_sides_vertices.append(hexagon_half_point)
        small_sides_vertices.append(small_sides_vertices_for_vertex[1])
    
    return small_sides_vertices, small_side_length

def draw_central_tri_star(tur, center, tri_star_length, upright_triangle_vertices):
    tri_star_vertices = []
    for vertex in upright_triangle_vertices:
        tur.teleport(center[0], center[1])
        heading = tur.towards(vertex[0], vertex[1])
        tur.setheading(heading)
        tur.forward(tri_star_length)
        tri_star_vertices.append([tur.pos()[0], tur.pos()[1]])
    return tri_star_vertices

def draw_lines_from_tri_star_to_small_triangle_vertices(tur, tri_star_vertices, small_sides_vertices, print_labels=False):
    def connect_by_indices(tur, tri_star_index, small_sides_indeces, tri_star_vertices, small_sides_vertices):
        tri_star_point = tri_star_vertices[tri_star_index]
        small_side_first_point = small_sides_vertices[small_sides_indeces[0]]
        small_side_second_point = small_sides_vertices[small_sides_indeces[1]]
        tur.teleport(tri_star_point[0], tri_star_point[1])
        tur.goto(small_side_first_point[0], small_side_first_point[1])
        tur.teleport(tri_star_point[0], tri_star_point[1])
        tur.goto(small_side_second_point[0], small_side_second_point[1])
    
    if print_labels:
        label_points(tur, small_sides_vertices, "v")
        label_points(tur, tri_star_vertices, "t", "green")
    
    connect_by_indices(tur, 0, [12, 2], tri_star_vertices, small_sides_vertices)
    connect_by_indices(tur, 1, [8, 0], tri_star_vertices, small_sides_vertices)
    connect_by_indices(tur, 2, [6, 14], tri_star_vertices, small_sides_vertices)

def draw_lines_between_small_triangle_vertices(tur, small_sides_vertices):
    def connect_by_indices(tur, small_sides_origin_indices, small_sides_destination_indices, small_sides_vertices):
        for i in range(0, len(small_sides_origin_indices)):
            origin_index = small_sides_origin_indices[i]
            destination_index = small_sides_destination_indices[i]
            origin_point = small_sides_vertices[origin_index]
            destination_point = small_sides_vertices[destination_index]
            tur.teleport(origin_point[0], origin_point[1])
            tur.goto(destination_point[0], destination_point[1])

    connect_by_indices(tur, [0, 3, 6, 9, 12, 15], [5, 8, 11, 14, 17, 2], small_sides_vertices)

def extract_pentagon_vertices(small_sides_vertices, tri_star_vertices, circle_center):
    def extract_central_pentagons(small_sides_vertices, tri_star_vertices, circle_center):
        top_left_pentagon = [circle_center, tri_star_vertices[1], small_sides_vertices[8], small_sides_vertices[6], tri_star_vertices[2]]
        top_right_pentagon = [circle_center, tri_star_vertices[0], small_sides_vertices[2], small_sides_vertices[0], tri_star_vertices[1]]
        bottom_pentagon = [circle_center, tri_star_vertices[2], small_sides_vertices[14], small_sides_vertices[12], tri_star_vertices[0]]
        return [top_left_pentagon, top_right_pentagon, bottom_pentagon]

    def extract_squashed_pentagons(small_sides_vertices, tri_star_vertices):
        top_pentagon = [tri_star_vertices[1], small_sides_vertices[0], small_sides_vertices[5], small_sides_vertices[3], small_sides_vertices[8]]
        bottom_left_pentagon = [tri_star_vertices[2], small_sides_vertices[6], small_sides_vertices[11], small_sides_vertices[9], small_sides_vertices[14]]
        bottom_right_pentagon = [tri_star_vertices[0], small_sides_vertices[12], small_sides_vertices[17], small_sides_vertices[15], small_sides_vertices[2]]
        return [top_pentagon, bottom_left_pentagon, bottom_right_pentagon]

    central_pentagons = extract_central_pentagons(small_sides_vertices, tri_star_vertices, circle_center)
    squashed_pentagons = extract_squashed_pentagons(small_sides_vertices, tri_star_vertices)
    pentagons = central_pentagons
    pentagons += squashed_pentagons
    return pentagons

def draw_pentagon_center_to_vertices_lines(tur, pentagons):
    def draw_lines_from_center_to_vertices(tur, center, vertices):
        for vertex in vertices:
            tur.teleport(center[0], center[1])
            tur.goto(vertex[0], vertex[1])

    for pentagon in pentagons:
        pentagon_center = find_regular_polygon_center(pentagon)
        draw_lines_from_center_to_vertices(tur, pentagon_center, pentagon)

def heading_halfway_between_consecutive_vertices(tur, center, vertex1, vertex2, ind):
    tur.teleport(center[0], center[1])
    vertex1_heading = tur.towards(vertex1[0], vertex1[1]) if tur.towards(vertex1[0], vertex1[1]) != 0 else 360
    tur.teleport(vertex1[0], vertex1[1])
    tur.teleport(center[0], center[1])
    vertex2_heading = tur.towards(vertex2[0], vertex2[1]) if tur.towards(vertex2[0], vertex2[1]) != 0 else 360
    tur.teleport(vertex2[0], vertex2[1])

    angle_difference = abs(vertex2_heading - vertex1_heading)
    if abs(vertex2_heading - vertex1_heading) > 180:
        difference_to_round_angle = 360 - max(vertex2_heading, vertex1_heading)
        angle_difference = difference_to_round_angle + min (vertex2_heading, vertex1_heading)

    return (vertex1_heading + angle_difference/2)

def draw_small_sides(tur, pentagon, center):    
    small_sides_vertices = []
    small_side_length = distance_between_two_points(center, pentagon[0]) * 2 / 5
    for i in range(0, 5):
        small_side_heading = heading_halfway_between_consecutive_vertices(tur, center, pentagon[i], pentagon[(i+1)%5], i)
        tur.setheading(small_side_heading)
        tur.teleport(center[0], center[1])
        tur.forward(small_side_length)
        small_sides_vertices.append(tur.pos())

    return small_sides_vertices

def find_pentagon_vertex_between_small_sides(tur, center, small_sides_vertex1, small_sides_vertex2, pentagon):
    tur.teleport(center[0], center[1])
    vertex1_heading = tur.towards(small_sides_vertex1[0], small_sides_vertex1[1])
    vertex2_heading = tur.towards(small_sides_vertex2[0], small_sides_vertex2[1])
    candidate_vertex = None
    for vertex in pentagon:
        pentagon_vertex_heading = tur.towards(vertex[0], vertex[1])

        if(pentagon_vertex_heading > vertex1_heading):
            candidate_vertex = vertex
            if(pentagon_vertex_heading < vertex2_heading):
                return vertex
            
        if(pentagon_vertex_heading < vertex2_heading):
            candidate_vertex = vertex

    return candidate_vertex

def connect_pentagon_vertex_to_small_sides(tur, small_sides_vertex1, small_sides_vertex2, pentagon_vertex):
    tur.teleport(small_sides_vertex1[0], small_sides_vertex1[1])
    tur.goto(pentagon_vertex[0], pentagon_vertex[1])
    tur.teleport(small_sides_vertex2[0], small_sides_vertex2[1])
    tur.goto(pentagon_vertex[0], pentagon_vertex[1])

def draw_small_sides_vertices_to_pentagon_vertices(tur, center, small_sides_vertices, pentagon):
    small_sides_number = len(small_sides_vertices)
    for i in range(0, small_sides_number):
        pentagon_vertex = find_pentagon_vertex_between_small_sides(tur, center, small_sides_vertices[i], small_sides_vertices[(i+1)%small_sides_number], pentagon)
        connect_pentagon_vertex_to_small_sides(tur, small_sides_vertices[i], small_sides_vertices[(i+1)%small_sides_number], pentagon_vertex)

def draw_pentagon_star(tur, pentagon, center):
    small_sides_vertices = draw_small_sides(tur, pentagon, center)
    draw_small_sides_vertices_to_pentagon_vertices(tur, center, small_sides_vertices, pentagon)

def draw_pentagons_stars(tur, pentagons):
    for pentagon in pentagons:
        pentagon_center = find_regular_polygon_center(pentagon)
        draw_pentagon_star(tur, pentagon, pentagon_center)
  
def draw_shape(tur, x, y, radius):
    circle_center = draw_circle(tur, x, y, radius)
    big_triangles_vertices = draw_big_triangles(tur, circle_center, radius)
    small_sides_vertices, small_side_length = draw_small_outer_triangles(tur, circle_center, big_triangles_vertices, distance_between_two_points(big_triangles_vertices[0], big_triangles_vertices[2]))
    tri_star_vertices = draw_central_tri_star(tur, circle_center, (small_side_length * 2) * 0.95, [big_triangles_vertices[-1], big_triangles_vertices[1], big_triangles_vertices[3]])
    draw_lines_from_tri_star_to_small_triangle_vertices(tur, tri_star_vertices, small_sides_vertices)
    draw_lines_between_small_triangle_vertices(tur, small_sides_vertices)
    pentagon_vertices = extract_pentagon_vertices(small_sides_vertices, tri_star_vertices, circle_center)
    draw_pentagon_center_to_vertices_lines(tur, pentagon_vertices)
    draw_pentagons_stars(tur, pentagon_vertices)