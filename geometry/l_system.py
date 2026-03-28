from libs.turtle_utils import teleport
# an l-system is a triplet:
# - alphabet: set of symbols
# - axiom: initial string of alphabet symbols
# - rules: given a symbol how to replace it each iteration

# l-system for turtle graphics
# alphabet:
# F forward
# B backward
# + turn right
# - turn left
# how much is a parameter

# axiom and rules depend on the particular fractal being drawn

# iterates iters times the rules upon the axiom
def calculate_l_system(iterations, axiom, rules):
    start_string = axiom
    if iterations == 0:
        return axiom
    end_string = ""
    for _ in range(iterations):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

# executes drawing commands
def draw_l_system(tur, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F' or cmd == 'A':
            tur.forward(distance)
        elif cmd == 'B':
            tur.backward(distance)
        elif cmd == '+':
            tur.right(angle)
        elif cmd == '-':
            tur.left(angle)

def draw_algae_l_system(tur, instructions, angle, distance):
    def get_turtle_position_and_heading(tur):
        return [[tur.xcor(), tur.ycor()], tur.heading()]

    lifo_queue = []
    for cmd in instructions:
        if cmd == 'F':
            tur.forward(distance)
        elif cmd == '+':
            tur.left(angle)
        elif cmd == '-':
            tur.right(angle)
        elif cmd == '[':
            lifo_queue.append(get_turtle_position_and_heading(tur))
        elif cmd == ']':
            position_and_heading = lifo_queue.pop()
            teleport(tur, position_and_heading[0])
            tur.setheading(position_and_heading[1])

def algae():
    setup = {}
    setup["axiom"] = "-X"
    setup["rules"] =  {"X":"F+[[X]-X]-F[-FX]+X", "F":"FF"}
    setup["iterations"] = 6 
    setup["angle"] = 25
    setup["length"] = 8
    return setup

def koch_snowflake():
    setup = {}
    setup["axiom"] = "F---F---F"
    setup["rules"] =  {"F":"F+F--F+F"}
    setup["iterations"] = 3 # TOP: 7
    setup["angle"] = 60
    setup["length"] = 10
    return setup

def quadratic_koch_snowflake():
    setup = {}
    setup["axiom"] = "F+F+F+F"
    setup["rules"] =  {"F":"F-F+F+FFF-F-F+F"}
    setup["iterations"] = 2 # TOP: 6
    setup["angle"] = 90
    setup["length"] = 10
    return setup

def crystal():
    setup = {}
    setup["axiom"] = "F+F+F+F"
    setup["rules"] =  {"F":"FF+F++F+F"}
    setup["iterations"] = 3 # TOP: 6
    setup["angle"] = 90
    setup["length"] = 10
    return setup

def quadratic_koch_snowflake():
    setup = {}
    setup["axiom"] = "F--F"
    setup["rules"] =  {"F":"F-F+F+F-F"}
    setup["iterations"] = 4 # TOP: 6
    setup["angle"] = 90
    setup["length"] = 10
    return setup

def peano_gosper_curve():
    setup = {}
    setup["axiom"] = "FX"
    setup["rules"] =  {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
    setup["iterations"] = 4 # TOP: 6
    setup["angle"] = 60
    setup["length"] = 10
    return setup    

def hex_lsystem():
    setup = {}
    setup["axiom"] = "F+F+F+F+F+A"
    setup["rules"] =  {"A": "F-F-F-F-F-B", "B": "F+F+F+F+C+F", "C": "F+F+F+F+F+A"}
    setup["iterations"] = 3 # TOP: 6
    setup["angle"] = 60
    setup["length"] = 50
    return setup

def pentapleyxity():
    setup = {}
    setup["axiom"] = "F++F++F++F++F"
    setup["rules"] =  {"F":"F++F++F+++++F-F++F"}
    setup["iterations"] = 2
    setup["angle"] = 36
    setup["length"] = 20
    return setup   

def sierpinski_arrowhead():
    setup = {}
    setup["axiom"] = "YF"
    setup["rules"] =  {"X":"YF+XF+Y", 
                       "Y":"XF-YF-X"}
    setup["iterations"] = 7
    setup["angle"] = 60
    setup["length"] = 5
    return setup   

def levy_c_curve():
    setup = {}
    setup["axiom"] = "F"
    setup["rules"] =  {"F":"+F--F+", 
                       "Y":"XF-YF-X"}
    setup["iterations"] = 7
    setup["angle"] = 45
    setup["length"] = 5
    return setup       

