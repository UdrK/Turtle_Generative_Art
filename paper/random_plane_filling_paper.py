import random_plane_filling.plane_filling_stats as pfs
from random_plane_filling.plane_filling import fill_plane
from libs.stats import sum_stat, print_stats, initialize_stats
from svg_turtle import SvgTurtle
from time import time

## SETUP

initialize_stats(pfs.stat_ids, pfs.stat_descriptions, 0)

## CANVAS SETUP
tur = SvgTurtle(1920, 1080)
tur.fillcolor("white")
screen = tur.getscreen()
screen.bgcolor("black")
tur.color("white")

## SCRIPT
filename = "../Drawings/random_plane_filling.svg"
start = time()

fill_plane(tur)
tur.save_as(filename)

end = time()
timespan = end - start
sum_stat(pfs.DRAWING_TOTAL_TIME, timespan)
print_stats(filename.replace(".svg", ".txt"))