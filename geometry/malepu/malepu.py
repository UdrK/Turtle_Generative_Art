from libs.generic_draw import draw
from geometry.malepu.malepu_shapes import draw_shape
from geometry.malepu.malepu_concentric_circles import draw_concentric_circles_complex

draw_shape_parameters = {"tur": None, "radius1": 200, "radius2": 210, "center_radius1": 10, "center_radius2": 20}
draw(draw_concentric_circles_complex, draw_shape_parameters, False)