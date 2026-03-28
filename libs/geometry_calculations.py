import math

def distance_between_two_points(p1, p2):
    """
    Returns the distance between two points
    
    :param p1: [x, y] coordinates of the first point
    :param p2: [x, y] coordinates of the second point

    :return: the distance between the two given points as a float value 
    """
    return pythagoras_hypotenuse(p1[0]-p2[0], p1[1]-p2[1])

def pythagoras_hypotenuse(side1, side2):
    """
    Calculates the hypotenuse of a right triangle according to pythagoras theorem given the two sides lenghts
    
    :param side1: length of the first side
    :param side2: length of the second side

    :return: the length of the hypotenuse of the right triangle with sides of length side1 and side2
    """
    return math.sqrt((side1)**2 + (side2)**2)

def pythagoras_side(hypotenuse, side):
    """
    Calculates the side of a right triangle according to pythagoras theorem given the other side and the hypotenuse
    
    :param hypotenuse: length of the hypotenuse
    :param side2: length of the other side

    :return: the length of the side of the right triangle with other side of length side and hypotenuse of length hypotenuse
    """
    return math.sqrt(abs((hypotenuse)**2 - (side)**2))

def find_regular_polygon_center(vertices):
    """
    Returns the (x, y) coordinates of the center of a regular polygon (all sides and angles equal) given an array of [x, y] vertices
    
    :param vertices: [[x, y], ..] array of coordinates of the vertices of the regular polygon

    :return: [x, y] coordinates of the center (of mass) of the regular polygon with given vertices 
    """
    def average_x_y_coordinates(vertices):
        cx = 0
        cy = 0

        for x, y in vertices:
            cx += x
            cy += y

        cx /= len(vertices)
        cy /= len(vertices)

        return (cx, cy)
    return average_x_y_coordinates(vertices)

def ssa_triangle(a, b, A_deg):
    """
    Solves a triangle given two sides and an opposite angle (SSA).

    Args:
        a: The length of side a.
        b: The length of side b.
        A_deg: The measure of angle A in degrees.

    Returns:
        A list of possible triangle solutions, where each solution is a tuple
        of (a, b, c, A_deg, B_deg, C_deg).
        Returns an empty list if no triangle can be formed or the case is invalid.
    """
    # Convert angle A to radians
    A = math.radians(A_deg)

    # Law of sines: sin(B)/b = sin(A)/a
    # Compute the height from side b
    h = b * math.sin(A)

    solutions = []

    if a < h:
        # No solution: side a is too short to reach side b
        return "No triangle possible."

    elif a == h:
        # One right triangle
        B = math.asin(b * math.sin(A) / a)
        B_deg = math.degrees(B)
        C_deg = 180 - A_deg - B_deg
        c = math.sqrt(b**2 + a**2 - 2*a*b*math.cos(math.radians(C_deg)))
        solutions.append((round(B_deg, 2), round(C_deg, 2), round(c, 2)))

    elif a >= b:
        # One solution
        B = math.asin(b * math.sin(A) / a)
        B_deg = math.degrees(B)
        C_deg = 180 - A_deg - B_deg
        c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C_deg)))
        solutions.append((round(B_deg, 2), round(C_deg, 2), round(c, 2)))

    else:
        # Two possible triangles
        B1 = math.asin(b * math.sin(A) / a)
        B2 = math.pi - B1

        B1_deg = math.degrees(B1)
        B2_deg = math.degrees(B2)

        C1_deg = 180 - A_deg - B1_deg
        C2_deg = 180 - A_deg - B2_deg

        if C1_deg > 0:
            c1 = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C1_deg)))
            solutions.append((round(B1_deg, 2), round(C1_deg, 2), round(c1, 2)))

        if C2_deg > 0:
            c2 = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C2_deg)))
            solutions.append((round(B2_deg, 2), round(C2_deg, 2), round(c2, 2)))

    return solutions