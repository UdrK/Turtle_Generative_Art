"""
Legacy turtle utility functions.

Prefer TGA_Turtle methods from libs.tga_turtle instead of importing from this module.
"""

import warnings

_DEPRECATION_MESSAGE = (
    "{name} is deprecated; use TGA_Turtle.{name}() instead of libs.turtle_utils.{name}()."
)


def _warn_deprecated(name):
    warnings.warn(_DEPRECATION_MESSAGE.format(name=name), DeprecationWarning, stacklevel=3)


# region Forward


def forward_without_drawing(tur, distance, heading=None):
    _warn_deprecated("forward_without_drawing")
    if heading is not None:
        tur.setheading(heading)
    without_drawing(
        lambda tur, distance: tur.forward(distance),
        {"tur": tur, "distance": distance},
    )
    return [tur.xcor(), tur.ycor()]


def forward_optional_draw(tur, distance, draw=True, heading=None):
    _warn_deprecated("forward_optional_draw")
    if heading is not None:
        tur.setheading(heading)
    if draw:
        tur.forward(distance)
        return tur.position()
    return forward_without_drawing(tur, distance, heading)


def forward_dashed(tur, distance, dash_proportions=(1.25, 1), heading=None):
    _warn_deprecated("forward_dashed")

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

    if heading is not None:
        tur.setheading(heading)

    tur.forward(first_and_last_line_length)
    i = 0
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
    _warn_deprecated("forward_and_reset")

    def _forward_and_reset(tur, distance):
        starting_point = tur.position()
        tur.forward(distance)
        arriving_point = (tur.xcor(), tur.ycor())
        tur.teleport(starting_point[0], starting_point[1])
        return arriving_point

    if not draw:
        return without_drawing(_forward_and_reset, {"tur": tur, "distance": distance})
    return _forward_and_reset(tur, distance)


def forward(tur, distance):
    _warn_deprecated("forward")
    tur.forward(distance)


# endregion


def without_drawing(method, keyword_arguments):
    _warn_deprecated("without_drawing")
    tur = keyword_arguments["tur"]
    is_pen_down = tur.isdown()
    if is_pen_down:
        tur.penup()
    result = method(**keyword_arguments)
    if is_pen_down:
        tur.pendown()
    return result


def invariant_draw(method, keyword_arguments):
    _warn_deprecated("invariant_draw")
    tur = keyword_arguments["tur"]
    original_position = tur.pos()
    original_heading = tur.heading()
    method_result = method(**keyword_arguments)
    tur.teleport(original_position[0], original_position[1])
    tur.setheading(original_heading)
    return method_result


def teleport(tur, point):
    _warn_deprecated("teleport")
    tur.teleport(point[0], point[1])


def calculate_circle_center(tur, radius):
    _warn_deprecated("calculate_circle_center")
    original_heading = tur.heading()
    tur.setheading(tur.heading() + 90)
    circle_center = forward_and_reset(tur, radius, False)
    tur.setheading(original_heading)
    return circle_center


def circle_and_return_center(tur, radius, extent=None, steps=None):
    _warn_deprecated("circle_and_return_center")
    circle_center = calculate_circle_center(tur, radius)
    if extent is not None or steps is not None:
        tur.circle(radius, extent, steps)
    else:
        tur.circle(radius)
    return circle_center


def circle_centered_at_turtle(tur, radius, extent=None, steps=None):
    _warn_deprecated("circle_centered_at_turtle")

    def draw_circle_centered_at_turtle(tur, radius, extent=None, steps=None):
        tur.setheading(0)
        teleport(tur, [tur.xcor(), tur.ycor() - radius])
        if extent is not None or steps is not None:
            tur.circle(radius, extent, steps)
        else:
            tur.circle(radius)

    params = {"tur": tur, "radius": radius, "extent": extent, "steps": steps}
    return invariant_draw(draw_circle_centered_at_turtle, params)
