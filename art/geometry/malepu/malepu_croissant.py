from libs.geometry_calculations import distance_between_two_points, ssa_triangle


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
    goto_croissant_vertex_params = {"radius": radius, "angle": angle}
    croissant_vertex = tur.without_drawing(draw_arc, goto_croissant_vertex_params)
    step_points = arc_stepping_method(tur, radius, 360 - 2 * angle, 23)
    return [circle_starting_point, croissant_vertex, step_points]


def draw_semicircle(tur, radius, angle):
    circle_starting_point = tur.pos()
    goto_croissant_vertex_params = {"radius": radius, "angle": angle}
    croissant_vertex = tur.without_drawing(draw_arc, goto_croissant_vertex_params)
    draw_arc(tur, radius, 360 - 2 * angle)
    return [circle_starting_point, croissant_vertex]


def connect_steps(tur, large_step_points, small_step_points):
    for i in range(len(large_step_points)):
        tur.teleport(large_step_points[i])
        step_heading = tur.towards(small_step_points[i])
        distance_between_steps = distance_between_two_points(
            large_step_points[i], small_step_points[i]
        )
        tur.setheading(step_heading)
        tur.forward_dashed(distance_between_steps)


def draw_croissant(
    tur,
    radius_large_edge,
    radius_small_edge,
    angle,
    angle_multiplier=2,
    smaller_arc_distance_offset=100,
    arc_stepping_method=None,
):
    original_heading = tur.heading()
    [large_circle_starting_point, croissant_vertex] = draw_semicircle(
        tur, radius_large_edge, angle
    )

    tur.teleport(
        large_circle_starting_point[0],
        large_circle_starting_point[1] - smaller_arc_distance_offset,
    )
    small_circle_angle = (
        tur.towards(croissant_vertex) * angle_multiplier
    )

    tur.setheading(original_heading)
    [small_circle_starting_point, croissant_vertex] = draw_semicircle(
        tur, radius_small_edge, small_circle_angle
    )


def draw_evenly_sectioned_croissant(
    tur,
    radius_large_edge,
    radius_small_edge,
    angle,
    arc_stepping_method,
    angle_multiplier=2,
    smaller_arc_distance_offset=100,
):
    original_heading = tur.heading()
    [large_circle_starting_point, croissant_vertex, large_step_points] = (
        draw_stepped_semicircle(tur, radius_large_edge, angle, arc_stepping_method)
    )

    tur.teleport(
        large_circle_starting_point[0],
        large_circle_starting_point[1] - smaller_arc_distance_offset,
    )
    small_circle_angle = tur.towards(croissant_vertex) * angle_multiplier

    tur.setheading(original_heading)
    [small_circle_starting_point, croissant_vertex, small_step_points] = (
        draw_stepped_semicircle(
            tur, radius_small_edge, small_circle_angle, arc_stepping_method
        )
    )

    connect_steps(tur, large_step_points, small_step_points)


def calculate_radial_inner_circle_step_points(
    tur, radius_small_edge, large_circle_center, small_circle_center, large_step_points
):
    radii_center = [small_circle_center[0], small_circle_center[1] + 100]
    distance_between_radii_center_and_small_circle_center = distance_between_two_points(
        small_circle_center, radii_center
    )

    inner_circle_step_points = []

    for point in large_step_points:
        tur.teleport(radii_center)
        point_heading = tur.towards(point)
        ssa_triangle_a_angle = 270 - point_heading
        distance_to_inner_circle = ssa_triangle(
            radius_small_edge,
            distance_between_radii_center_and_small_circle_center,
            ssa_triangle_a_angle,
        )
        tur.setheading(point_heading)
        step_point = tur.forward_without_drawing(distance_to_inner_circle[0][2])
        inner_circle_step_points.append(step_point)

    return inner_circle_step_points


def calculate_large_semicircle_steps(
    tur, large_circle_center, radius_large_edge, croissant_vertex, number_of_steps=22
):
    steps = []
    steps_per_side = int(number_of_steps / 2)
    middle_step = [large_circle_center[0], large_circle_center[1] + radius_large_edge]
    tur.teleport(middle_step)
    tur.setheading(90)
    angle_between_steps = 11

    for _ in range(steps_per_side):
        tur.teleport(large_circle_center)
        tur.left(angle_between_steps)
        step = tur.forward_without_drawing(radius_large_edge)
        steps.insert(0, step)

    steps.append(middle_step)
    tur.setheading(90)

    for _ in range(steps_per_side):
        tur.teleport(large_circle_center)
        tur.right(angle_between_steps)
        step = tur.forward_without_drawing(radius_large_edge)
        steps.append(step)

    return steps


def draw_radially_sectioned_croissant(
    tur,
    radius_large_edge,
    radius_small_edge,
    angle,
    angle_multiplier=2,
    smaller_arc_distance_offset=100,
):
    original_heading = tur.heading()
    large_circle_center = tur.calculate_circle_center(radius_large_edge)
    [large_circle_starting_point, croissant_vertex] = draw_semicircle(
        tur, radius_large_edge, angle
    )
    large_step_points = calculate_large_semicircle_steps(
        tur, large_circle_center, radius_large_edge, croissant_vertex
    )

    tur.teleport(
        large_circle_starting_point[0],
        large_circle_starting_point[1] - smaller_arc_distance_offset,
    )
    small_circle_angle = tur.towards(croissant_vertex) * angle_multiplier
    tur.setheading(original_heading)

    small_circle_center = tur.calculate_circle_center(radius_small_edge)
    [small_circle_starting_point, croissant_vertex] = draw_semicircle(
        tur, radius_small_edge, small_circle_angle
    )
    small_step_points = calculate_radial_inner_circle_step_points(
        tur,
        radius_small_edge,
        large_circle_center,
        small_circle_center,
        large_step_points,
    )
    connect_steps(tur, large_step_points, small_step_points)


def draw_evenly_croissant_complex(tur):
    original_heading = tur.heading()
    tur.teleport([0, -400])
    draw_croissant(tur, 400, 300, 45, 2.02)
    tur.teleport([0, -390])
    tur.setheading(original_heading)
    draw_evenly_sectioned_croissant(
        tur, 390, 310, 52.5, draw_arc_in_equi_steps, 2, 115
    )


def draw_croissant_complex(tur):
    original_heading = tur.heading()
    tur.teleport([0, -400])
    draw_croissant(tur, 400, 300, 45, 2.02)
    tur.teleport([0, -390])
    tur.setheading(original_heading)
    draw_radially_sectioned_croissant(tur, 390, 310, 52.5, 2, 115)
