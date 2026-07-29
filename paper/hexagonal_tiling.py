from libs.tga_turtle import TGA_Turtle
from libs.geometry_calculations import find_regular_polygon_center

def drawing(tur: TGA_Turtle):
    columns = 10
    rows = 6
    hex_index = 0
    original_heading = tur.heading()
    hex_centers = []
    hex_results = None
    hex_size = 100

    tur.teleport((-700, -525))

    for i in range(columns):
        first_hex_in_column = {}
        for j in range(rows):
            hex_results = hex(tur, hex_size, hex_index, i)
            tur.teleport(hex_results[1])
            tur.setheading(original_heading)
            hex_centers.append(hex_results[2])
            if j == 0:
                first_hex_in_column = hex_results
            hex_index += 1
        tur.teleport(first_hex_in_column[0])

        if (i % 2 != 0):
            tur.right(360/6)
            tur.forward_without_drawing(hex_size)

        tur.setheading(original_heading)

def hex(tur: TGA_Turtle, size, hex_index=0, column_index=0):
    angle = 360 / 6
    vertices = []
    results = []
    for i in range(6):
        tur.forward(size)
        tur.left(angle)
        vertices.append(tur.pos())
        if (column_index % 2 == 0 and i == 1) or (column_index % 2 != 0 and i == 0) or i == 3:
            results.append(tur.pos())

    center = find_regular_polygon_center(vertices)
    results.append(center)
    tur.teleport(center)
    #tur.write(hex_index)
    return results

        
## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[1920, 1080])
tur.color("white")
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")

drawing(tur)

tur.save_as("../Drawings/hexagonal_tiling.svg")
print("Saved: hexagonal_tiling.svg")