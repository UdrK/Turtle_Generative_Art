from libs.generic_draw import draw
from art.geometry.malepu.malepu_shapes import draw_circle_with_crescent_circle_inside
from art.geometry.malepu.malepu_concentric_circles import draw_concentric_circles_complex

draw_shape_parameters = {"tur": None, "radius": 210, "arc_angle": 250}
draw(draw_circle_with_crescent_circle_inside, draw_shape_parameters, False)