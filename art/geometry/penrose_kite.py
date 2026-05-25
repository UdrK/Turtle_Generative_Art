import turtle
import math
from svg_turtle import SvgTurtle

##
## utility methods
##
PHI = (1 + math.sqrt(5)) / 2

def sas(long, short, angle):
    return math.sqrt(long*long + short*short - 2*long*short*math.cos(math.radians(angle)))

def isosceles_base(side, angle=72):
    return side * math.sqrt(2*(1-math.cos(math.radians(angle/2))))

def long_side(short):
    return PHI * short

def base_kite(tur, short, long):
    long = long_side(short)
    tur.left(54)
    tur.forward(long)
    tur.left(108)
    tur.forward(short)
    tur.left(36)
    tur.forward(short)
    tur.left(108)
    tur.forward(long)

##
## Penrose kite recursive method
##
alpha = 108
theta = 54
phi = 18

def penrose_kite(tur, A, B, recursion_level):
    if(recursion_level == 0):
        base_kite(tur, A, B)
    else:
        small_B = isosceles_base(A)
        small_A = sas(B - A, small_B, 36)
        penrose_kite(tur, small_A, small_B, recursion_level-1)
        tur.left(alpha)
        tur.forward(B)
        tur.left(alpha)
        tur.forward(A)
        tur.left(theta)
        penrose_kite(tur, small_B, A, recursion_level-1)
        tur.right(phi)
        penrose_kite(tur, small_B, A, recursion_level-1)
        tur.left(alpha)
        tur.forward(A)
        tur.left(alpha)
        tur.forward(B)