from libs.turtle_utils import forward_dashed, teleport, forward_optional_draw, circle_and_return_center, invariant_draw, circle_centered_at_turtle, forward_dashed
from libs.geometry_shapes import draw_oval, draw_triangle
from geometry.malepu.malepu_croissant import draw_croissant_complex, draw_evenly_croissant_complex

def draw_overlapping_triangles(tur, triangle_side, draw_lower_side = False):
    angle = 360 / 3
    halfway_points = []
    tur.setheading(0)

    for i in range(5):
        if i == 0:
            forward_optional_draw(tur, triangle_side, draw_lower_side)
            tur.setheading(tur.heading()+angle)
        else:
            tur.forward(triangle_side / 2)
            if i % 2 == 0:
                tur.setheading(tur.heading()+angle)
            else:
                halfway_points.append(tur.position())
    
    tur.setheading(0)
    teleport(tur, halfway_points[0])
    for i in range(4):
        if i == 0 or i == 3:
            forward_optional_draw(tur, triangle_side / 4, draw_lower_side)
        else:
            tur.forward(triangle_side)
        tur.setheading(tur.heading()+angle)

def draw_crescent_circle(tur, radius, step_size = 3, number_of_crescents = 6):
    def get_points_alongside_circle(tur, radius, step_size, number_of_crescents):
        points = []
        tur.penup()
        for _ in range(number_of_crescents):
            tur.circle(radius, 360 - step_size)
            points.append(tur.position())
        tur.pendown()
        return points

    def reset_heading(tur, original_heading, iteration):
        tur.setheading(original_heading + step_size * iteration)

    def draw_crescent(tur, radius, step_size, iteration):
        tur.circle(radius, 180 - step_size * 2 * iteration)

    original_heading = tur.heading()
    circle_center = circle_and_return_center(tur, radius)
    crescents_starting_points = get_points_alongside_circle(tur, radius, step_size, number_of_crescents)
    i = 1
    for point in crescents_starting_points:
        teleport(tur, point)
        reset_heading(tur, original_heading, i)
        draw_crescent(tur, radius, step_size, i)
        i += 1

    return circle_center

def draw_eye(tur, radius, arc_length):
    def draw_with_fill(method, keyword_arguments):
        tur = keyword_arguments['tur']
        tur.begin_fill()

        method_result = method(**keyword_arguments)

        tur.end_fill()
        return method_result
    
    oval_lower_center = tur.pos()
    [oval_center, oval_height] = invariant_draw(draw_oval, {"tur": tur, "radius": radius, "arc_length": arc_length})
    original_heading = tur.heading()
    tur.setheading(original_heading)

    small_oval_radius = radius * 0.8
    small_oval_height = oval_height * small_oval_radius / radius

    distance_between_ovals = (oval_height - small_oval_height)

    teleport(tur, [oval_lower_center[0], oval_lower_center[1]+distance_between_ovals])
    actual_small_oval_height = draw_oval(tur, small_oval_radius, arc_length)

    filled_circle_radius = radius / 7
    outlining_circle_radius = filled_circle_radius * 1.5
    teleport(tur, oval_center)
    draw_with_fill(circle_centered_at_turtle, {"tur": tur, "radius": filled_circle_radius})
    circle_centered_at_turtle(tur, outlining_circle_radius)

def draw_segmented_non_triangle(tur, sides_length, starter_heading=5):
    def draw_arc(tur, sides_length):
        arc_points = []
        radius_direction = -1 if starter_heading > 90 else 1
        radius = 0.5*sides_length * radius_direction
        angles = [35, 15, 15, 15, 25]
        for i in range(len(angles)):
            tur.circle(radius, -1*angles[i])
            arc_points.append(tur.pos())
        return arc_points

    def connect_vertex_to_arc_points(tur, triangle_vertex, arc_points):
        for point in arc_points:
            teleport(tur, triangle_vertex)
            tur.goto(point[0], point[1])

    tur.setheading(starter_heading)
    triangle_vertex = tur.pos()
    tur.forward(sides_length)
    arc_points = draw_arc(tur, sides_length)
    connect_vertex_to_arc_points(tur, triangle_vertex, arc_points)

def large_concentric_triangles(tur, side):
    multiplication_factor = 0.03
    original_heading = tur.heading()
    draw_triangle(tur, side)
    tur.setheading(original_heading + 30)
    forward_optional_draw(tur, side*multiplication_factor, False)
    tur.setheading(original_heading)
    draw_triangle(tur, side*0.95, forward_dashed)

def draw_shape(tur):
    draw_croissant_complex(tur)
    # large_concentric_triangles(tur, 500)