import art.random_plane_filling.plane_filling_stats as pfs
from art.random_plane_filling.plane_filling import fill_plane
from libs.stats import sum_stat, print_stats, initialize_stats
from libs.tga_turtle import TGA_Turtle
from time import time

## SETUP

initialize_stats(pfs.stat_ids, pfs.stat_descriptions, 0)

## CANVAS SETUP
tur = TGA_Turtle(is_svg=True, canvas_size=[1920, 1080])
inner = tur.turtle
inner.fillcolor("white")
screen = inner.getscreen()
screen.bgcolor("black")
inner.color("white")

## SCRIPT
filename = "../Drawings/random_plane_filling.svg"
start = time()

fill_plane(tur)
tur.save_as(filename)

end = time()
timespan = end - start
sum_stat(pfs.DRAWING_TOTAL_TIME, timespan)
print_stats(filename.replace(".svg", ".txt"))
