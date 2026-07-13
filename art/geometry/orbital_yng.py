from libs.generic_draw import draw

def shape(tur, radius):
    def draw_vertical_center_line(tur, radius):
        tur.setheading(90)
        tur.forward_without_drawing(radius)
        tur.setheading(-90)
        tur.forward(radius*2)

    def draw_horizontal_mid_line(tur, radius):
        length = radius * 0.2
        tur.forward_without_drawing(radius)
        tur.setheading(180)
        tur.forward(length)
        tur.forward_without_drawing(2*(radius*0.8))
        tur.forward(length)

    def draw_diagonal_circles(tur, radius, direction=-1):
        tur.setheading(45+(direction*90))
        tur.forward_without_drawing(radius * 0.65)
        tur.circle_centered_at_turtle(radius * 0.05)

    def draw_arc(tur, radius, direction=-1):
        origin = tur.pos()
        tur.setheading(90)
        tur.forward_without_drawing((-direction)*radius * 0.2)
        start = tur.pos()
        control_point_1 = (direction*radius*0.45, (-direction)*radius*0.2)
        control_point_2 = (direction*radius*0.55, direction*radius*0.5)
        end = [origin[0], origin[1]+direction*radius]

        tur.cubic_bezier(start, control_point_1, control_point_2, end)

    tur.circle_centered_at_turtle(radius, steps=80)
    tur.circle_centered_at_turtle(radius * 0.2, steps=80)

    methods_args = {"tur": tur, "radius": radius}
    upper_arc_args=  {"tur": tur, "radius": radius, "direction": 1}
    tur.invariant_draw(draw_vertical_center_line, methods_args)
    tur.invariant_draw(draw_horizontal_mid_line, methods_args)
    tur.invariant_draw(draw_diagonal_circles, methods_args)
    tur.invariant_draw(draw_diagonal_circles, upper_arc_args)
    tur.invariant_draw(draw_arc, methods_args)
    tur.invariant_draw(draw_arc, upper_arc_args)
    

draw_shape_parameters = {"tur": None, 
                        "radius": 300}
draw(shape, draw_shape_parameters, True)
