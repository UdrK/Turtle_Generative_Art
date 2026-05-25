import uuid

from libs.tga_turtle import TGA_Turtle


def draw(
    method,
    keyword_arguments,
    is_svg=True,
    filename="",
    canvas_size=[1920, 1080],
    bg_color="black",
    stroke_color="white",
):
    """
    Runs a drawing method with a configured TGA_Turtle instance.

    Usage:
    from libs.generic_draw import draw

    def draw_shape(tur):
        pass

    draw_shape_parameters = {"tur": None}
    draw(draw_shape, draw_shape_parameters, False)

    :param method: function in which a turtle does things
    :param keyword_arguments: a dictionary of arguments to pass to method,
        should contain a "tur" key (value is overwritten by a new TGA_Turtle)
    :return: returns whatever method returns
    """
    tur = TGA_Turtle(is_svg=is_svg, canvas_size=canvas_size)
    w = canvas_size[0]
    h = canvas_size[1]
    inner = tur.turtle
    inner.speed(0)
    inner.color(stroke_color)
    inner.hideturtle()
    screen = inner.getscreen()
    screen.screensize(w, h)
    screen.bgcolor(bg_color)
    keyword_arguments["tur"] = tur

    result = method(**keyword_arguments)

    screen.mainloop()
    if is_svg:
        if filename == "":
            filename = str(uuid.uuid4())
        tur.save_as(f"{filename}.svg")

    return result
