# region Forward

def forward_without_drawing(tur, distance, heading=None):
    """
    Move turtle forward without drawing

    :param tur: the turtle
    :param distance: distance to move the turtle forward for
    :param heading: optional heading to set for the turtle before moving forward
    :return: coordinates of turtle after forward
    """
    if(heading != None):
        tur.setheading(heading)

    without_drawing(lambda tur, distance: tur.forward(distance), {"tur": tur, "distance": distance})
    return [tur.xcor(), tur.ycor()]

def forward_optional_draw(tur, distance, draw=True, heading=None):
    """
    Move turtle forward with or without drawing

    :param tur: the turtle
    :param distance: distance to move the turtle forward for
    :param draw: decides if forward is drawn or not
    :param heading: optional heading to set for the turtle before moving forward
    :return: coordinates of turtle after forward
    """
    if(heading != None):
        tur.setheading(heading)

    result = None

    if(draw):
        tur.forward(distance)
        result = tur.position()
    else:
        result = forward_without_drawing(tur, distance, heading)
    return result

def forward_dashed(tur, distance, dash_proportions=(1.25, 1), heading=None):
    """
    Move turtle forward in a dashed line - - - fashion

    :param tur: the turtle
    :param distance: distance to move the turtle forward for
    :param dash_proportions: a couple of number, will be used in a proportion a : 100 = x : distance to figure out the proportions of the dashes
    :param heading: optional heading to set for the turtle before moving forward
    :return: coordinates of turtle after forward
    """
    def draw_space(tur, space):
        tur.penup()
        tur.forward(space_length)
        tur.pendown()

    line_length = 475 * dash_proportions[0] / 100
    space_length = 475 * dash_proportions[1] / 100

    distance_traveled = 0

    while True:
        distance_traveled += space_length

        if distance_traveled > distance:
            distance_traveled -= space_length
            break

        distance_traveled += line_length

        if distance_traveled > distance:
            distance_traveled -= line_length
            break

    gap = distance - distance_traveled
    first_and_last_line_length = gap / 2
    distance_to_travel = distance_traveled
    distance_traveled = 0

    # print(f"Distance to forward {distance}")
    # print(f"Distance to travel {distance_to_travel}")
    # print(f"line_length {line_length}")
    # print(f"space_length {space_length}")
    # print(f"first_and_last_line_length {first_and_last_line_length}")

    if(heading != None):
        tur.setheading(heading)

    i = 0
    tur.forward(first_and_last_line_length)
    while distance_traveled < distance_to_travel:
        if i % 2 == 0:
            draw_space(tur, space_length)
            distance_traveled += space_length
        else:
            tur.forward(line_length)
            distance_traveled += line_length
        i += 1
    
    tur.forward(first_and_last_line_length)
    return [tur.xcor(), tur.ycor()]

def forward_and_reset(tur, distance, draw=True):
    """
    Goes forward a distance and then goes backwards the same distance. The turtle ends where it started

    :param tur: the turtle
    :param distance: the distance to go forward
    :param draw: does the turtle draw while going forward and backward
    :return: the x, y coordinates of the point the turtle arrived at after forward
    """
    def forward_and_reset(tur, distance):
        starting_point = tur.position()
        tur.forward(distance)
        arriving_point = (tur.xcor(), tur.ycor())
        tur.teleport(starting_point[0], starting_point[1])
        return arriving_point

    if not draw:
        return without_drawing(forward_and_reset, {"tur": tur, "distance": distance})
    
    return forward_and_reset(tur, distance)

def forward(tur, distance):
    """
    Simple forward

    :param tur: the turtle
    :param distance: the distance to go forward
    """
    tur.forward(distance)

# endregion

def without_drawing(method, keyword_arguments):
    """
    Runs method without drawing. Leaves turtle pen status unchanged
    
    :param method: function in which a turtle does things
    :param keyword_arguments: a dictionary of arguments to pass to method, 
        should contain a "tur" key with Turtle() value
    :return: returns whatever method returns
    """
    tur = keyword_arguments['tur']

    is_pen_down = tur.isdown()

    if is_pen_down:
        tur.penup()

    result = method(**keyword_arguments)

    if is_pen_down:
        tur.pendown()
    
    return result

def invariant_draw(method, keyword_arguments):
    """
    Draws a given method and reset the initial conditions (position, heading) of the turtle
    
    :param method: function in which a turtle does things
    :param keyword_arguments: a dictionary of arguments to pass to method, 
        should contain a "tur" key with Turtle() value
    :return: returns whatever method returns
    """
    tur = keyword_arguments['tur']
    original_position = tur.pos()
    original_heading = tur.heading()

    method_result = method(**keyword_arguments)

    tur.teleport(original_position[0], original_position[1])
    tur.setheading(original_heading)

    return method_result

def teleport(tur, point):
    """
    Teleports turtle to a given point

    :param tur: the turtle
    :param point: the point where the turtle is teleported to
    """
    tur.teleport(point[0], point[1])

def calculate_circle_center(tur, radius):
    """
    Calculate center of circle that would be drawn given the radius

    :param tur: the turtle
    :param radius: the radius of the circle to draw
    """
    original_heading = tur.heading()
    tur.setheading(tur.heading()+90)
    circle_center = forward_and_reset(tur, radius, False)
    tur.setheading(original_heading)
    return circle_center

def circle_and_return_center(tur, radius, extent=None, steps=None):
    """
    Draws circle and returns its center

    :param tur: the turtle
    :param radius: the radius of the circle to draw
    :param extent: the extent of the circle to draw, will not draw entire circle but an arc
    :param steps: steps used to approximate a circle
    """
    circle_center = calculate_circle_center(tur, radius)
    tur.circle(radius, extent, steps)
    return circle_center

def circle_centered_at_turtle(tur, radius, extent=None, steps=None):
    """
    Draws circle and returns its center

    :param tur: the turtle
    :param radius: the radius of the circle to draw
    :param extent: the extent of the circle to draw, will not draw entire circle but an arc
    :param steps: steps used to approximate a circle
    """
    def draw_circle_centered_at_turtle(tur, radius, extent=None, steps=None):
        tur.setheading(0)
        teleport(tur, [tur.xcor(), tur.ycor()-radius])
        tur.circle(radius, extent, steps)
    
    params = {"tur": tur, "radius": radius, "extent": extent, "steps":steps}
    return invariant_draw(draw_circle_centered_at_turtle, params)