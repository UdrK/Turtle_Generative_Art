from libs.generic_draw import draw
from art.geometry.malepu.malepu_shapes import draw_shape
from art.geometry.malepu.malepu_concentric_circles import draw_concentric_circles_complex

draw_shape_parameters = {"tur": None, "radius1": 210, "radius2": 200, "center_radius1": 20, "center_radius2": 10}
draw(draw_concentric_circles_complex, draw_shape_parameters, True)