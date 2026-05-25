def draw_center(tur, center_radius1, center_radius2):

    tur.begin_fill()
    tur.circle_centered_at_turtle(center_radius1)
    tur.end_fill()

    tur.circle_centered_at_turtle(center_radius2)


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
    tur.circle_centered_at_turtle(radius2)


def draw_concentric_circles_complex(tur, center_radius1, center_radius2, radius1, radius2):
    draw_center(tur, center_radius1, center_radius2)
    draw_radii(tur, center_radius2, radius1)
    draw_concentric_circles(tur, radius1, radius2)
