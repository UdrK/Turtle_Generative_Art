import random
import time as t
from shapely.geometry import Polygon
import random_plane_filling.plane_filling_stats as pfs
from libs.utils import time_method
from libs.turtle_utils import teleport, forward_and_reset, without_drawing
from libs.stats import sum_stat

polygons = []

## UTILITY METHODS

def get_nearby_polygons(polygons, x, y, distance):
    """
    Given a list of polygons, returns a sublist of polygons in distance from the given x, y coordinates

    :param polygons: list of polygons
    :param x: x coordinate 
    :param y: y coordinate
    :param distace: polygons in distance from x, y will be returned
    :return: a list of polygons in distance from x, y
    """
    start = t.time()
    polys_nearby = [p for p in polygons if abs(p['center_x'] - x) < distance and abs(p['center_y'] - y) < distance]
    end = t.time()
    timespan = end - start
    sum_stat(pfs.TOTAL_TIME_GETTING_NEARBY_POLYGONS, timespan)
    return polys_nearby

## \

def detect_intersection(a, b):
    """
    Detects if there's an intersection between polygons a and b

    :param a: dictionary with a key value pair "points": [(x, y), ...]
    :param b: same as a
    """
    a_polygon = Polygon(a["points"])
    b_polygon = Polygon(b["points"])

    sum_stat(pfs.CHECKS_FOR_INTERSECTION, 1)

    return a_polygon.intersects(b_polygon)


def detect_any_intersection(polygon, distance_to_check=0):
    """
    Searches for intersections between given polygon and any other polygon drawn

    :param polygon: dictionary with a key value pair "points": [(x, y), ...]
    :param distance_to_check: only looks for intersection with polygons center in this distance
    """
    polygon_center_x = polygon["center_x"]
    polygon_center_y = polygon["center_y"]

    # without_drawing(lambda tur, x, y: tur.goto(x, y), {"tur": tur, "x": x, "y": y})
    nearby_polygons = time_method(get_nearby_polygons, {"polygons": polygons, "x": polygon_center_x, "y": polygon_center_y, "distance": distance_to_check})
    sum_stat(pfs.TOTAL_TIME_GETTING_NEARBY_POLYGONS, nearby_polygons[1])

    for p in nearby_polygons[0]:
        if detect_intersection(polygon, p):
            return True
    
    return False


def draw_regular_polygon(tur, size, sides):
    """
    :param tur: the turtle
    :param size: size of the polygon
    :param sides: how many sides does the polygon have
    :return: a dictionary defining the polygon drawn
    """
    angle = 360 / sides
    points = []
    vertices_sum_x = 0
    vertices_sum_y = 0

    for _ in range(sides):
        vertices_sum_x += tur.xcor()
        vertices_sum_y += tur.ycor()
        outside_polygon_vertex = concentric_polygon_vertex(tur, size, sides, angle)
        points.append(outside_polygon_vertex)
        tur.forward(size)
        tur.right(angle)
        
    return {
        "center_x": vertices_sum_x / sides,
        "center_y": vertices_sum_y / sides,
        "points": points
    }


def concentric_polygon_vertex(tur, size, sides, angle, size_factor=0.05):
    """
    Returns the x, y coordinates of the concentric polygon vertex calculated from parameters

    :param tur: the turtle
    :param size: size of the polygon
    :param sides: how many sides does the polygon have
    :param angle: the angle between sides of the polygon
    :size_factor: multiplicator for the size to determine how much larger/smaller the concentric polygon is
    :return: the x, y coordinates of the concentric polygon vertex
    """
    original_heading = tur.heading()
    distance = size * size_factor
    concentric_polygon_vertex_heading = original_heading+((1+0.25*(sides-2))*angle)

    tur.setheading(concentric_polygon_vertex_heading)
    concentric_polygon_vertex = forward_and_reset(tur, distance, False)
    tur.setheading(original_heading)

    return concentric_polygon_vertex


def trace_polygon(polygon_drawing_method, polygon_drawing_parameters, draw):
    """
    Traces regular polygon without necessarely drawing it

    :param polygon_drawing_method: method that draws a polygon
    :param polygon_drawing_parameters: parameters for the aforementioned method
    :param draw: if true draws the polygon, else only traces it (the return stays the same)
    :return: return of the method
    """
    if not draw:
        return without_drawing(polygon_drawing_method, polygon_drawing_parameters)
    return polygon_drawing_method(**polygon_drawing_parameters)


def draw_polygon_without_colliding(polygon_drawing_method, polygon_drawing_parameters, min_max_x, min_max_y):
    """
    Tries to draw the polygon without intersecting other polygons until it succedes

    :param polygon_drawing_method: method that draws a polygon
    :param polygon_drawing_parameters: parameters for the aforementioned method
    :param min_max_x: tuple that contains the min and max x coordinates of the screen
    :param min_max_y: tuple that contains the min and max y coordinates of the screen
    """
    def __get_random_coordinates(min_max_x, min_max_y):
        random_x = random.randint(min_max_x[0], min_max_x[1])
        random_y = random.randint(min_max_y[0], min_max_y[1])
        return (random_x, random_y)

    can_be_drawn = False
    while not can_be_drawn:
        polygon_start = __get_random_coordinates(min_max_x, min_max_y)
        tur = polygon_drawing_parameters["tur"]
        teleport(tur, polygon_start)
        polygon_to_draw = trace_polygon(polygon_drawing_method, polygon_drawing_parameters, False)
        can_be_drawn = not detect_any_intersection(polygon_to_draw, 200)
        if can_be_drawn:
            trace_polygon(polygon_drawing_method, polygon_drawing_parameters, True)
            polygons.append(polygon_to_draw)
        else:
            sum_stat(pfs.POLYGONS_TRACED_NOT_DRAWN, 1)


def fill_plane(tur, output=False):
    """
    Fills the plane of randomly positioned polygons
    """
    polygons_drawn_number = 0
    iterations = 8
    sizes = calculate_sizes(60, iterations)
    numbers = calculate_number_of_polygons(3, iterations)

    for i in range(iterations):
        polygons_drawn_number = 1
        while polygons_drawn_number <= numbers[i]:
            if polygons_drawn_number % 100 == 0 and output:
                print("polys drawn {}".format(polygons_drawn_number))
            random_heading = random.randint(0, 360)
            tur.setheading(random_heading)
            regular_polygon_parameters = {"tur": tur, "size": sizes[i], "sides": 6}
            draw_polygon_without_colliding(draw_regular_polygon, regular_polygon_parameters,  (-700, 700), (-250, 500))
            tur.setheading(0)
            polygons_drawn_number += 1


def calculate_sizes(first_size, iterations):
    """
    Calculates the sizes of polygons to be drawn
    """
    sizes = [first_size]
    for i in range(2, iterations+1):
        size = first_size / (i ** 1.85)
        sizes.append(size)

    print("Sizes of polygons to be drawn: {}".format(sizes))
    return sizes


def calculate_number_of_polygons(first_number, iterations):
    """
    Calculates the sizes of polygons to be drawn
    """
    numbers = []
    for i in range(1, iterations+1):
        number = (i*first_number)**2
        numbers.append(number)

    print("Number of polygons to be drawn: {}".format(numbers))
    return numbers


