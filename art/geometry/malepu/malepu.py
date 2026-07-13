from libs.generic_draw import draw
from art.geometry.malepu.malepu_shapes import draw_circle_with_crescent_circle_inside, draw_eye
from art.geometry.malepu.malepu_concentric_circles import draw_concentric_circles_complex
from art.geometry.malepu.malepu_croissant import Bthree_part_croissant, three_part_croissant

draw_shape_parameters = {"tur": None, 
                        "radius": 300,
                        "arc_length": 50}
draw(draw_eye, draw_shape_parameters, True)
