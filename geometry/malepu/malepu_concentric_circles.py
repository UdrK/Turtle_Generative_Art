from libs.turtle_utils import circle_centered_at_turtle, forward_without_drawing, teleport, forward_dashed

def draw_center(tur, center_radius1, center_radius2):

    tur.begin_fill()
    circle_centered_at_turtle(tur, center_radius1)
    tur.end_fill()

    circle_centered_at_turtle(tur, center_radius2)

def draw_radii(tur, center_radius2, radius1):
    radii_number = 36
    radii_angle = 360 / radii_number

    center = tur.position()

    forward_length = radius1 - center_radius2

    for i in range(radii_number):
        tur.setheading(i*radii_angle)
        forward_without_drawing(tur, center_radius2)
        forward_dashed(tur, forward_length)
        teleport(tur, center)

def draw_concentric_circles(tur, radius1, radius2):
    circle_centered_at_turtle(tur, radius1)
    circle_centered_at_turtle(tur, radius2)

def draw_concentric_circles_complex(tur, center_radius1, center_radius2, radius1, radius2):
    draw_center(tur, center_radius1, center_radius2)
    draw_radii(tur, center_radius2, radius1)
    # draw_rotating_circle(tur, radius1/2)
    draw_concentric_circles(tur, radius1, radius2)