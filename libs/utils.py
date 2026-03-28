from time import time
from datetime import datetime
import math

def save_setup_file(filename, setup_data):
    """
    Saves the setup data to a file.
    
    :param filename: name of the file to save the setup data
    :param setup_data: array of strings to be saved in the file as separate lines
    """
    with open(filename, "a") as f:
        for data in setup_data:
            f.write(data+"\n")

def rotate_point(x, y, z, angle_x, angle_y):
    """
    Rotates a point (x, y, z) around the X, Y axes by the given angles.
    
    :param x: x coordinate of the point
    :param y: y coordinate of the point
    :param z: z coordinate of the point
    :param angle_x: angle in degrees to rotate around the X axis
    :param angle_y: angle in degrees to rotate around the Y axis
    """
    # Rotate around X axis
    rad_x = math.radians(angle_x)
    cos_x = math.cos(rad_x)
    sin_x = math.sin(rad_x)
    y1 = y * cos_x - z * sin_x
    z1 = y * sin_x + z * cos_x

    # Rotate around Y axis
    rad_y = math.radians(angle_y)
    cos_y = math.cos(rad_y)
    sin_y = math.sin(rad_y)
    x2 = x * cos_y + z1 * sin_y
    z2 = -x * sin_y + z1 * cos_y

    return x2, y1, z1, z2  # 2D projection

def time_method(method, keyword_arguments):
    """
    Times how long it takes to execute the given method
    
    :param method: function
    :param keyword_arguments: a dictionary of arguments to pass to method
    :return: returns a couple (method_result, execution_time)
    """
    start_clock = time()
    method_result = method(**keyword_arguments)
    end_clock = time()

    return(method_result, end_clock-start_clock)

def get_filepath(prefix, postfix):
    """
    Generates a unique filename based on the current date and time.

    :param prefix: prefix for the filename
    :param postfix: postfix for the filename
    """
    dt = datetime.now()
    string_datetime = dt.strftime("%d-%m-%Y_%H%M%S")
    return "{}_{}_{}".format(prefix, string_datetime, postfix)

def label_point(tur, point, label, label_color="red"):
    """
    Moves turtle to given point if necessary and writes label on screen at that point, returns the turtle to the original position

    :param tur: the turtle
    :param point: the point to be labeled on screen
    :param label: the label to write at point
    """
    original_color = tur.pencolor()
    tur.pencolor(label_color)
    original_turtle_position = tur.pos()
    changed_position = False
    if(tur.pos()[0] != point[0] or tur.pos()[1] != point[1]):
        tur.teleport(point[0], point[1])
        changed_position = True
    
    tur.write(label)
    if changed_position:
        tur.teleport(original_turtle_position[0], original_turtle_position[1])
    tur.pencolor(original_color)

def label_points(tur, points, label_suffix, label_color="red"):
    """
    Moves turtle to given points and labels them. Uses label_point(tur, point, label) under the hood

    :param tur: the turtle
    :param point: the point to be labeled on screen
    :param label: the label to write at point
    """
    i = 0
    for point in points:
        label_point(tur, point, "{}{}".format(label_suffix, i), label_color)
        i += 1