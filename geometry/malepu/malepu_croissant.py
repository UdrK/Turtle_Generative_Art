from libs.turtle_utils import forward_dashed, teleport, without_drawing, calculate_circle_center, forward_without_drawing, forward_dashed
from libs.geometry_calculations import distance_between_two_points, ssa_triangle

"""
def radial_signs_test(tur):
    circle_center = tur.pos()
    other_circle_center = [tur.xcor(), tur.ycor()+80]
    outside_point = [tur.xcor()-200, tur.ycor()+170]
    circle_radius = 150
    circle_centered_at_turtle(tur, 2)
    circle_centered_at_turtle(tur, circle_radius)
    teleport(tur, other_circle_center)
    circle_centered_at_turtle(tur, 2)
    teleport(tur, outside_point)
    circle_centered_at_turtle(tur, 2)

    distance_between_centers = distance_between_two_points(circle_center, other_circle_center)

    teleport(tur, other_circle_center)
    outside_point_heading = tur.towards(outside_point[0], outside_point[1])
    a_angle = 270 - outside_point_heading
    last_side = ssa_triangle(circle_radius, distance_between_centers, a_angle)
    
    distance_between_points = distance_between_two_points(outside_point, other_circle_center)
    print(last_side)
    tur.setheading(outside_point_heading)
    tur.penup()
    tur.forward(last_side[0][2])
    tur.pendown()
    tur.forward(distance_between_points-last_side[0][2])
"""

def draw_arc(tur, radius, angle):
    tur.circle(radius, angle)
    return tur.pos()

def draw_arc_in_equi_steps(tur, radius, angle, number_of_steps):
    step_angle = angle / number_of_steps
    step_points = []
    for _ in range(number_of_steps):
        tur.circle(radius, step_angle)
        step_points.append(tur.pos())
    return step_points

def draw_stepped_semicircle(tur, radius, angle, arc_stepping_method):
    circle_starting_point = tur.pos()
    goto_croissant_vertex_params = {"tur": tur, "radius": radius, "angle": angle}
    croissant_vertex = without_drawing(draw_arc, goto_croissant_vertex_params)
    step_points = arc_stepping_method(tur, radius, 360 - 2 * angle, 23)
    return [circle_starting_point, croissant_vertex, step_points]

def draw_semicircle(tur, radius, angle):
    circle_starting_point = tur.pos()
    goto_croissant_vertex_params = {"tur": tur, "radius": radius, "angle": angle}
    croissant_vertex = without_drawing(draw_arc, goto_croissant_vertex_params)
    draw_arc(tur, radius, 360 - 2 * angle)
    return [circle_starting_point, croissant_vertex]

def connect_steps(tur, large_step_points, small_step_points):
    for i in range(len(large_step_points)):
        teleport(tur, large_step_points[i])
        step_heading = tur.towards(small_step_points[i][0], small_step_points[i][1])
        distance_between_steps = distance_between_two_points(large_step_points[i], small_step_points[i])
        tur.setheading(step_heading)
        forward_dashed(tur, distance_between_steps)

def draw_croissant(tur, radius_large_edge, radius_small_edge, angle, angle_multiplier=2, smaller_arc_distance_offset=100, arc_stepping_method=None):
    original_heading = tur.heading()
    [large_circle_starting_point, croissant_vertex] = draw_semicircle(tur, radius_large_edge, angle)

    tur.teleport(large_circle_starting_point[0], large_circle_starting_point[1]-smaller_arc_distance_offset)
    small_circle_angle = tur.towards(croissant_vertex[0], croissant_vertex[1])*angle_multiplier

    tur.setheading(original_heading)
    [small_circle_starting_point, croissant_vertex] = draw_semicircle(tur, radius_small_edge, small_circle_angle)

def draw_evenly_sectioned_croissant(tur, radius_large_edge, radius_small_edge, angle, arc_stepping_method, angle_multiplier=2, smaller_arc_distance_offset=100):
    original_heading = tur.heading()
    [large_circle_starting_point, croissant_vertex, large_step_points] = draw_stepped_semicircle(tur, radius_large_edge, angle, arc_stepping_method)

    tur.teleport(large_circle_starting_point[0], large_circle_starting_point[1]-smaller_arc_distance_offset)
    small_circle_angle = tur.towards(croissant_vertex[0], croissant_vertex[1])*angle_multiplier

    tur.setheading(original_heading)
    [small_circle_starting_point, croissant_vertex, small_step_points] = draw_stepped_semicircle(tur, radius_small_edge, small_circle_angle, arc_stepping_method)

    connect_steps(tur, large_step_points, small_step_points)

def calculate_radial_inner_circle_step_points(tur, radius_small_edge, large_circle_center, small_circle_center, large_step_points):
    radii_center = [small_circle_center[0], small_circle_center[1]+100]
    distance_between_radii_center_and_small_circle_center = distance_between_two_points(small_circle_center, radii_center)

    inner_circle_step_points = []

    for point in large_step_points:
        teleport(tur, radii_center)
        point_heading = tur.towards(point[0], point[1])
        ssa_triangle_a_angle = 270 - point_heading
        distance_to_inner_circle = ssa_triangle(radius_small_edge, distance_between_radii_center_and_small_circle_center, ssa_triangle_a_angle)
        tur.setheading(point_heading)
        step_point = forward_without_drawing(tur, distance_to_inner_circle[0][2])
        inner_circle_step_points.append(step_point)
    
    return inner_circle_step_points

def calculate_large_semicircle_steps(tur, large_circle_center, radius_large_edge, croissant_vertex, number_of_steps=22):
    steps = []
    steps_per_side = int(number_of_steps / 2)
    middle_step = [large_circle_center[0], large_circle_center[1]+radius_large_edge]
    teleport(tur, middle_step)
    tur.setheading(90)
    angle_between_steps = 11

    for _ in range(steps_per_side):
        teleport(tur, large_circle_center)
        tur.left(angle_between_steps)
        step = forward_without_drawing(tur, radius_large_edge)
        steps.insert(0, step)

    steps.append(middle_step)
    tur.setheading(90)

    for _ in range(steps_per_side):
        teleport(tur, large_circle_center)
        tur.right(angle_between_steps)
        step = forward_without_drawing(tur, radius_large_edge)
        steps.append(step)

    return steps

def draw_radially_sectioned_croissant(tur, radius_large_edge, radius_small_edge, angle, angle_multiplier=2, smaller_arc_distance_offset=100):
    original_heading = tur.heading()
    large_circle_center = calculate_circle_center(tur, radius_large_edge)
    [large_circle_starting_point, croissant_vertex] = draw_semicircle(tur, radius_large_edge, angle)
    large_step_points = calculate_large_semicircle_steps(tur, large_circle_center, radius_large_edge, croissant_vertex)

    tur.teleport(large_circle_starting_point[0], large_circle_starting_point[1]-smaller_arc_distance_offset)
    small_circle_angle = tur.towards(croissant_vertex[0], croissant_vertex[1])*angle_multiplier
    tur.setheading(original_heading)
    
    small_circle_center = calculate_circle_center(tur, radius_small_edge)
    [small_circle_starting_point, croissant_vertex] = draw_semicircle(tur, radius_small_edge, small_circle_angle)
    small_step_points = calculate_radial_inner_circle_step_points(tur, radius_small_edge, large_circle_center, small_circle_center, large_step_points)
    connect_steps(tur, large_step_points, small_step_points)

def draw_evenly_croissant_complex(tur):
    original_heading = tur.heading()
    teleport(tur, [0,-400])
    draw_croissant(tur, 400, 300, 45, 2.02)
    teleport(tur, [0,-390])
    tur.setheading(original_heading)
    draw_evenly_sectioned_croissant(tur, 390, 310, 52.5, draw_arc_in_equi_steps, 2, 115)

def draw_croissant_complex(tur):
    original_heading = tur.heading()
    teleport(tur, [0,-400])
    draw_croissant(tur, 400, 300, 45, 2.02)
    teleport(tur, [0,-390])
    tur.setheading(original_heading)
    draw_radially_sectioned_croissant(tur, 390, 310, 52.5, 2, 115)