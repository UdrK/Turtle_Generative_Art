from numpy import interp

def calculate_parabola(parabola, x_value):
    return parabola(x_value)

def map_value_between_ranges(value, range1, range2):
    return interp(value, range1, range2)