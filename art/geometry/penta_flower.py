
from libs.geometry_calculations import find_circle_center_passing_through_two_points

def draw_base_polygons(tur, radius, inner_circle_radius):
    def draw_big_circle(tur, radius):
        tur.circle_centered_at_turtle(radius)

    def draw_pentagons(tur, radius):
        first_pentagon_vertices = tur.polygon_centered_at_turtle(radius, 5, 90)
        second_pentagon_vertices = tur.polygon_centered_at_turtle(radius, 5, 90+((360/5)/2), True)
        return first_pentagon_vertices, second_pentagon_vertices
    
    def draw_vertical_divider(tur, radius):
        tur.setheading(90)
        tur.forward(radius)
        tur.teleport(starting_point)

    def draw_inner_circle(tur, radius):
        tur.circle_centered_at_turtle(radius)

    starting_point = tur.pos()

    draw_big_circle(tur, radius)
    first_pentagon_vertices, second_pentagon_vertices = draw_pentagons(tur, radius)
    draw_vertical_divider(tur, radius)
    draw_inner_circle(tur, inner_circle_radius)

    return first_pentagon_vertices, second_pentagon_vertices

def get_inner_circle_pentagon_intersections(tur, inner_circle_radius, polygon_vertices, drawing_center):
    inner_circle_vertices = []
    for i in range(len(polygon_vertices)):
        tur.teleport(drawing_center)
        tur.setheading(tur.towards(polygon_vertices[i]))
        tur.forward_without_drawing(inner_circle_radius)
        inner_circle_vertices.append(tur.pos())
    
    return inner_circle_vertices

def draw_petal_aux_circles(tur, inner_circle_vertices, petal_aux_circle_radius):
    circle_centers = []
    for i in range(len(inner_circle_vertices)):
        center = find_circle_center_passing_through_two_points(inner_circle_vertices[i], inner_circle_vertices[(i+1)%len(inner_circle_vertices)], petal_aux_circle_radius)
        circle_centers.append(center[1])
        tur.teleport(center[1])
        tur.circle_centered_at_turtle(petal_aux_circle_radius)

    return circle_centers

def draw_half_petal(tur, starting_point, end_point, aux_circle_center, aux_circle_radius, drawing_center, radius, direction):
    def draw_circle_part(tur, starting_point, aux_circle_center, aux_circle_radius, extent):
        tur.teleport(starting_point)
        tur.setheading(tur.towards(aux_circle_center)-90)
        tur.circle(aux_circle_radius, extent)

    def calculate_bezier_control_point_1(tur, drawing_center, radius, petal_vertex):
        tur.teleport(drawing_center)
        tur.setheading(tur.towards(petal_vertex))
        tur.forward_without_drawing(radius*0.75)
        return tur.pos()

    def calculate_bezier_control_point_2(tur, end_point, direction, angle = 11.452238697599995, distance = 78.13988660686356):
        tur.setheading(tur.towards(end_point))
        tur.right(direction*angle)
        tur.forward_without_drawing(distance)
        return tur.pos()

    draw_circle_part(tur, starting_point, aux_circle_center, aux_circle_radius, direction*45)

    circle_end_point = tur.pos()

    bez_point_1 = calculate_bezier_control_point_1(tur, drawing_center, radius, end_point)
    tur.teleport(circle_end_point)
    bez_point_2 = calculate_bezier_control_point_2(tur, end_point, direction)
    tur.teleport(circle_end_point)

    debug = False
    if(debug):
        print(f"bez_point_1 {bez_point_1}")
        print(f"bez_point_2 {bez_point_2}")
        tur.teleport(bez_point_1)
        tur.dot()
        tur.write("1")
        tur.teleport(bez_point_2)
        tur.dot()
        tur.write("2")
        tur.teleport(circle_end_point)

    tur.cubic_bezier(circle_end_point, bez_point_2, bez_point_1, end_point)
    return circle_end_point

def draw_half_inner_circle(tur, inner_circle_radius):
    tur.setheading(270)
    tur.forward_without_drawing(inner_circle_radius)
    tur.setheading(0)
    tur.circle(inner_circle_radius, extent=-180)

def calculate_small_petals_vertices(tur, petals_base_points, drawing_center, inner_circle_radius):
    vertices = []
    for base_point in petals_base_points:
        tur.teleport(base_point)
        heading = tur.towards(drawing_center) - 180
        tur.setheading(heading)
        tur.forward_without_drawing(inner_circle_radius)
        vertices.append(tur.pos())
        
    return vertices

def draw_half_small_petal(tur, starting_point, end_point, drawing_center, radius, direction):
    def calculate_bezier_control_point_1(tur, drawing_center, radius, petal_vertex):
        tur.teleport(drawing_center)
        tur.setheading(tur.towards(petal_vertex))
        tur.forward_without_drawing(radius*0.75)
        return tur.pos()
    
    def calculate_bezier_control_point_2(tur, end_point, direction, angle = -25.452238697599995, distance = 38.13988660686356):
        tur.setheading(tur.towards(end_point))
        tur.right(direction*angle)
        tur.forward_without_drawing(distance)
        return tur.pos()

    bez_point_1 = calculate_bezier_control_point_1(tur, drawing_center, radius, end_point)
    tur.teleport(starting_point)
    bez_point_2 = calculate_bezier_control_point_2(tur, end_point, direction)
    tur.teleport(starting_point)

    debug = False
    if(debug):
        print(f"bez_point_1 {bez_point_1}")
        print(f"bez_point_2 {bez_point_2}")
        tur.teleport(bez_point_1)
        tur.dot()
        tur.write("1")
        tur.teleport(bez_point_2)
        tur.dot()
        tur.write("2")
        tur.teleport(starting_point)

    tur.cubic_bezier(starting_point, bez_point_2, bez_point_1, end_point)

def draw_inner_flower(tur, petals_base_point, petal_aux_circle_center, petal_aux_circle_radius, direction, extent):
    tur.teleport(petals_base_point)
    tur.setheading(tur.towards(petal_aux_circle_center)-90)
    tur.circle(petal_aux_circle_radius, extent=direction*extent)

def flower(tur, radius):
    drawing_center = tur.pos()
    inner_circle_radius = radius*0.25
    petal_aux_circle_radius = inner_circle_radius*0.75

    first_pentagon_vertices, second_pentagon_vertices = draw_base_polygons(tur, radius, inner_circle_radius)

    inner_circle_vertices = get_inner_circle_pentagon_intersections(tur, inner_circle_radius, second_pentagon_vertices, drawing_center)

    circle_centers = draw_petal_aux_circles(tur, inner_circle_vertices, petal_aux_circle_radius)

    petals_vertices = [first_pentagon_vertices[0], first_pentagon_vertices[1], first_pentagon_vertices[2]]
    petals_base_points = [inner_circle_vertices[0], inner_circle_vertices[1], inner_circle_vertices[2]]
    petal_aux_circle_centers = [circle_centers[0], circle_centers[1], circle_centers[4]]

    tur.pensize(5)
    tur.color("purple")

    p1 = draw_half_petal(tur, petals_base_points[0], petals_vertices[0], petal_aux_circle_centers[2], petal_aux_circle_radius, drawing_center, radius, -1)
    p2 = draw_half_petal(tur, petals_base_points[0], petals_vertices[1], petal_aux_circle_centers[0], petal_aux_circle_radius, drawing_center, radius, 1)
    p3 = draw_half_petal(tur, petals_base_points[1], petals_vertices[1], petal_aux_circle_centers[0], petal_aux_circle_radius, drawing_center, radius, -1)
    p4 = draw_half_petal(tur, petals_base_points[1], petals_vertices[2], petal_aux_circle_centers[1], petal_aux_circle_radius, drawing_center, radius, 1)
    p5 = draw_half_petal(tur, petals_base_points[2], petals_vertices[2], petal_aux_circle_centers[1], petal_aux_circle_radius, drawing_center, radius, -1)

    small_petals_starting_points = [p1, p2, p3, p4, p5]

    tur.teleport(drawing_center)
    draw_half_inner_circle(tur, inner_circle_radius)

    small_petals_vertices = calculate_small_petals_vertices(tur, petals_base_points, drawing_center, 2*inner_circle_radius)

    draw_half_small_petal(tur, small_petals_starting_points[0], small_petals_vertices[0], drawing_center, 3*inner_circle_radius, -1)
    draw_half_small_petal(tur, small_petals_starting_points[1], small_petals_vertices[0], drawing_center, 3*inner_circle_radius, 1)
    draw_half_small_petal(tur, small_petals_starting_points[2], small_petals_vertices[1], drawing_center, 3*inner_circle_radius, -1)
    draw_half_small_petal(tur, small_petals_starting_points[3], small_petals_vertices[1], drawing_center, 3*inner_circle_radius, 1)
    draw_half_small_petal(tur, small_petals_starting_points[4], small_petals_vertices[2], drawing_center, 3*inner_circle_radius, -1)

    draw_inner_flower(tur, petals_base_points[0], petal_aux_circle_centers[0], petal_aux_circle_radius, -1, 102)
    draw_inner_flower(tur, petals_base_points[1], petal_aux_circle_centers[1], petal_aux_circle_radius, -1, 102)
    draw_inner_flower(tur, petals_base_points[0], petal_aux_circle_centers[2], petal_aux_circle_radius, 1, 51)
