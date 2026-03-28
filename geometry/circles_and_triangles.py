from libs.turtle_utils import invariant_draw, forward_without_drawing
from libs.geometry_calculations import pythagoras_side
from libs.utils import label_point

BIG_CIRCLE_RADIUS = 150
SMALL_CIRCLE_RADIUS = BIG_CIRCLE_RADIUS - (BIG_CIRCLE_RADIUS / 3.4)
CENTER_FULL_CIRCLE_RADIUS = center_FULL_CIRCLE_RADIUS = ((BIG_CIRCLE_RADIUS + 1/6 * SMALL_CIRCLE_RADIUS) * 0.234) / 2

def draw_circle_centered_on_coordinates(tur, x, y, radius, fill=False):
    def draw_circle_centered_on_coordinates_aux(tur, x, y, radius):
        tur.setheading(0)
        tur.teleport(x, y-radius)
        tur.circle(radius)

    if (fill):
        tur.begin_fill()

    draw_circle_args = {"tur": tur, "x": x, "y": y, "radius": radius}
    invariant_draw(draw_circle_centered_on_coordinates_aux, draw_circle_args)

    if (fill):
        tur.end_fill()

def draw_center_full_circle(tur, circle_size):
    draw_circle_centered_on_coordinates(tur, tur.xcor(), tur.ycor(), circle_size, True)
    return tur.position()

def draw_two_empty_circles(tur, position, direction, big_circle_radius, small_circle_radius, center_full_circle_radius):
    tur.teleport(position[0], position[1])
    forward_without_drawing(tur, small_circle_radius-center_full_circle_radius, direction+180)
    tur.setheading(direction-90)
    tur.circle(small_circle_radius)
    tur.circle(big_circle_radius)

def draw_triangle_from_horizontal_side_center(tur, position, heading, triangle_side):
    angle = 360 / 3
    tur.teleport(position[0], position[1])
    tur.setheading(heading+90)
    tur.forward(triangle_side/2)
    for _ in range(2):
        tur.setheading(tur.heading()+angle)
        tur.forward(triangle_side)
    tur.setheading(tur.heading()+angle)
    tur.forward(triangle_side/2)

def draw_big_triangle(tur, position, direction, triangle_side, center_full_circle_radius):
    def draw_vertical_line_with_circles(tur, position, direction, triangle_side, center_full_circle_radius):
        small_full_circle_radius = (center_full_circle_radius / 2.75)
        triangle_height = pythagoras_side(triangle_side, triangle_side/2)
        first_segment = triangle_height * 0.2476
        second_segment = (triangle_height * 0.6595) - first_segment
        third_segment =  triangle_height - second_segment - first_segment
        tur.teleport(position[0], position[1])
        tur.setheading(direction)
        tur.forward(center_full_circle_radius)
        tur.forward(first_segment)
        draw_circle_centered_on_coordinates(tur, tur.xcor(), tur.ycor(), small_full_circle_radius, True)
        tur.forward(second_segment-small_full_circle_radius)
        second_segment_position = tur.position()
        tur.forward(small_full_circle_radius)
        draw_circle_centered_on_coordinates(tur, tur.xcor(), tur.ycor(), small_full_circle_radius, True)
        tur.forward(third_segment+small_full_circle_radius)
        draw_circle_centered_on_coordinates(tur, tur.xcor(), tur.ycor(), small_full_circle_radius, True)
        tur.backward(small_full_circle_radius)
        return second_segment_position

    second_segment_position = draw_vertical_line_with_circles(tur, position, direction, triangle_side, center_full_circle_radius)
    draw_triangle_from_horizontal_side_center(tur, tur.position(), tur.heading(), triangle_side)
    return second_segment_position

def draw_half_drawing(tur, position, direction):
    def draw_small_triangle(tur, triangle_horizontal_side_half_point, triangle_side, direction):
        draw_triangle_from_horizontal_side_center(tur, triangle_horizontal_side_half_point, direction, triangle_side)

    draw_two_empty_circles(tur, position, direction, BIG_CIRCLE_RADIUS, SMALL_CIRCLE_RADIUS, CENTER_FULL_CIRCLE_RADIUS)
    second_segment_position = draw_big_triangle(tur, position, direction, BIG_CIRCLE_RADIUS*2, CENTER_FULL_CIRCLE_RADIUS)
    draw_small_triangle(tur, second_segment_position, (BIG_CIRCLE_RADIUS*2)*0.8408, direction-180)
    
def draw_shape(tur):
    drawing_center = draw_center_full_circle(tur, CENTER_FULL_CIRCLE_RADIUS)
    draw_half_drawing(tur, drawing_center, 270)
    draw_half_drawing(tur, drawing_center, 90)