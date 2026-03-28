from turtle import Turtle
from svg_turtle import SvgTurtle
import uuid

def draw(method, keyword_arguments, is_svg=True, filename="", canvas_size=[1920, 1080], bg_color="black", stroke_color="white"):
    """
    Runs method without drawing. Leaves turtle pen status unchanged
    
    :param method: function in which a turtle does things
    :param keyword_arguments: a dictionary of arguments to pass to method, 
        should contain a "tur" key with Turtle() value
    :return: returns whatever method returns
    """
    tur = keyword_arguments['tur']
    w = canvas_size[0]
    h = canvas_size[1]
    if is_svg:
        tur = SvgTurtle()
    else:
        tur = Turtle()
    tur.speed(0)
    tur.color(stroke_color)
    tur.hideturtle()
    screen = tur.getscreen()
    screen.screensize(w, h)
    screen.bgcolor(bg_color)
    keyword_arguments['tur'] = tur

    result = method(**keyword_arguments)

    screen.mainloop()
    if is_svg:
        if filename == "":
            filename = str(uuid.uuid4())
        tur.save_as(f"{filename}.svg")

    return result