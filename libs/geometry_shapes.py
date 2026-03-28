from libs.turtle_utils import forward, teleport, invariant_draw
from enum import IntEnum

class Direction(IntEnum):
    UP = 1
    DOWN = -1

def draw_triangle(tur, side, forward_strategy=forward):
    for _ in range(3):
        forward_strategy(tur, side)
        tur.left(120)

def draw_oval(tur, radius, arc_length):
    def draw_half_oval_half_side(tur, radius, arc_length):
        tur.circle(radius, arc_length)
        side_apex = tur.pos()
        return side_apex
    
    def draw_oval_side(tur, radius, arc_length, direction=Direction.UP):
        def draw_right_half_side(tur, radius, arc_length, direction):
            invariant_draw(draw_half_oval_half_side, {"tur": tur, "radius": radius, "arc_length": direction*arc_length})

        def draw_left_half_side_after_right(tur, radius, arc_length, direction):
            tur.setheading(tur.heading()+180)
            side_apex = invariant_draw(draw_half_oval_half_side, {"tur": tur, "radius": -1*radius, "arc_length": direction*arc_length})
            tur.setheading(tur.heading()-180)
            return side_apex
        
        oval_lower_curve_center = tur.pos()
        draw_right_half_side(tur, radius, arc_length, direction)
        side_apex = draw_left_half_side_after_right(tur, radius, arc_length, direction)

        oval_curves_apices_distance = abs(oval_lower_curve_center[1]-side_apex[1])
        upper_side_starting_point = [oval_lower_curve_center[0], oval_lower_curve_center[1]+oval_curves_apices_distance*2]
        oval_center = [oval_lower_curve_center[0], oval_lower_curve_center[1]+oval_curves_apices_distance]
        return [upper_side_starting_point, oval_center, oval_curves_apices_distance]
    
    [upper_side_center_point, oval_center, oval_height] = draw_oval_side(tur, radius, arc_length)
    teleport(tur, upper_side_center_point)
    tur.setheading(tur.heading()+180)
    draw_oval_side(tur, radius, arc_length, Direction.DOWN)

    return [oval_center, oval_height]