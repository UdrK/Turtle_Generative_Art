from strange_attractors.attractor import draw_attractor, lorenz_attractor
from svg_turtle import SvgTurtle

tur = SvgTurtle(1920, 1080)

attractor_params = {
    "x": 1,
    "y": 1,
    "z": 1,
    "sigma": 10,    
    "beta": 2/3,
    "rho": 28,
    "dt": 0.005
}

tur = draw_attractor(tur, lorenz_attractor, attractor_params)
tur.save_as("../Drawings/lorenz_attractor.svg")