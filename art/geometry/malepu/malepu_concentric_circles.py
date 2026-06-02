from libs.geometry_calculations import angle_between_intersecting_circles

def draw_center(tur, center_radius1, center_radius2):
    tur.begin_fill()
    tur.circle_centered_at_turtle(center_radius2)
    tur.end_fill()

    tur.circle_centered_at_turtle(center_radius1)


def draw_radii(tur, center_radius2, radius1):
    radii_number = 36
    radii_angle = 360 / radii_number

    center = tur.position()

    forward_length = radius1 - center_radius2

    for i in range(radii_number):
        tur.setheading(i * radii_angle)
        tur.forward_without_drawing(center_radius2)
        tur.forward_dashed(forward_length)
        tur.teleport(center)


def draw_concentric_circles(tur, radius1, radius2):
    tur.circle_centered_at_turtle(radius1)
    return tur.stepped_circle_centered_at_turtle(radius2, 8)

def draw_concentric_circles_with_radii(tur, center_radius1, center_radius2, radius1, radius2):
    draw_center(tur, center_radius1, center_radius2)
    draw_radii(tur, center_radius1, radius2)
    return draw_concentric_circles(tur, radius1, radius2)

def draw_inner_circles(tur, size, center_coordinate, circles_origins, center_radius):
    def draw_partial_circle(tur, size, pendown_extent, penup_extent):
        tur.circle(size, pendown_extent)
        tur.penup()
        tur.circle(size, penup_extent)
        tur.pendown()
        tur.circle(size, pendown_extent)

    center_angle = angle_between_intersecting_circles(size, center_radius)
    print(center_angle)

    for coordinate in circles_origins:
        tur.teleport(coordinate)
        center_heading = tur.towards(center_coordinate)
        tur.setheading(center_heading-90)
        draw_partial_circle(tur, size, 180 - (center_angle/2), center_angle)


def draw_concentric_circles_complex(tur, center_radius1, center_radius2, radius1, radius2):
    center_position = tur.position()
    steps = draw_concentric_circles_with_radii(tur, center_radius1, center_radius2, radius1, radius2)
    draw_inner_circles(tur, radius2 / 2, center_position, steps, center_radius1)
