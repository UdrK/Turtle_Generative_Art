from turtle import Turtle

class TGA_Turtle:

    def __init__(self, is_svg=False, canvas_size=None):
        if is_svg:
            from svg_turtle import SvgTurtle

            if canvas_size is not None:
                self.turtle = SvgTurtle(canvas_size[0], canvas_size[1])
            else:
                self.turtle = SvgTurtle()
        else:
            self.turtle = Turtle()

    # region movement

    def forward(self, quantity):
        return self.turtle.forward(quantity)

    def backward(self, quantity):
        return self.turtle.backward(quantity)

    def left(self, angle):
        return self.turtle.left(angle)

    def right(self, angle):
        return self.turtle.right(angle)

    def goto(self, *args):
        return self.turtle.goto(*args)

    def setheading(self, angle):
        return self.turtle.setheading(angle)

    def circle(self, *args, **kwargs):
        return self.turtle.circle(*args, **kwargs)

    def flat_arc(self, heading, radius, angle, debug=False):
        arc_edges = []

        self.setheading(heading)
        self.forward_optional_draw(radius, debug)
        arc_edges.append(self.position())
        self.setheading(heading+90)
        self.circle(radius, angle)
        arc_edges.append(self.position())

        return arc_edges

    def generic_arc(self, radius, angle):
        complementary_angle = 360 - angle
        self.setheading(complementary_angle/2)
        self.circle(radius, angle)

    # endregion

    # region state

    def position(self):
        return self.turtle.position()

    def pos(self):
        return self.turtle.pos()

    def heading(self):
        return self.turtle.heading()

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()

    def towards(self, *args):
        if len(args) == 1:
            point = args[0]
            return self.turtle.towards(point[0], point[1])
        return self.turtle.towards(args[0], args[1])

    # endregion

    # region pen control

    def penup(self):
        return self.turtle.penup()

    def pendown(self):
        return self.turtle.pendown()

    def pensize(self, width=None):
        return self.turtle.pensize(width)

    def pencolor(self, *args):
        return self.turtle.pencolor(*args)

    def fillcolor(self, *args):
        return self.turtle.fillcolor(*args)

    def color(self, *args):
        return self.turtle.color(*args)

    def isdown(self):
        return self.turtle.isdown()

    # endregion

    # region drawing

    def mark_spot(self, color="red"):
        original_pen_color = self.pencolor()
        self.pencolor(color)
        self.dot()
        self.pencolor(original_pen_color)

    def dot(self, size=None, *color):
        if color:
            return self.turtle.dot(size, *color)
        if size is not None:
            return self.turtle.dot(size)
        return self.turtle.dot()

    def begin_fill(self):
        return self.turtle.begin_fill()

    def end_fill(self):
        return self.turtle.end_fill()

    def write(self, text, move=False, align="left", font=("Arial", 8, "normal")):
        return self.turtle.write(text, move=move, align=align, font=font)

    # endregion

    # region display

    def hideturtle(self):
        return self.turtle.hideturtle()

    def showturtle(self):
        return self.turtle.showturtle()

    def speed(self, speed_value):
        return self.turtle.speed(speed_value)

    def getscreen(self):
        return self.turtle.getscreen()

    def save_as(self, filename):
        return self.turtle.save_as(filename)

    # endregion

    # region helpers

    def teleport(self, *args):
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            return self.turtle.teleport(args[0][0], args[0][1])
        return self.turtle.teleport(*args)

    def without_drawing(self, method, keyword_arguments):
        keyword_arguments = dict(keyword_arguments)
        keyword_arguments["tur"] = self
        is_pen_down = self.isdown()
        if is_pen_down:
            self.penup()
        result = method(**keyword_arguments)
        if is_pen_down:
            self.pendown()
        return result

    def invariant_draw(self, method, keyword_arguments):
        keyword_arguments = dict(keyword_arguments)
        keyword_arguments["tur"] = self
        original_position = self.pos()
        original_heading = self.heading()
        method_result = method(**keyword_arguments)
        self.teleport(original_position[0], original_position[1])
        self.setheading(original_heading)
        return method_result

    def forward_without_drawing(self, distance, heading=None):
        if heading is not None:
            self.setheading(heading)
        self.without_drawing(
            lambda tur, distance: tur.forward(distance),
            {"distance": distance},
        )
        return [self.xcor(), self.ycor()]

    def forward_optional_draw(self, distance, draw=True, heading=None):
        if heading is not None:
            self.setheading(heading)
        if draw:
            self.forward(distance)
            return self.position()
        return self.forward_without_drawing(distance, heading)

    def forward_dashed(self, distance, dash_proportions=(1.25, 1), heading=None):
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
            self.setheading(heading)

        self.forward(first_and_last_line_length)
        i = 0
        while distance_traveled < distance_to_travel:
            if i % 2 == 0:
                draw_space(self, space_length)
                distance_traveled += space_length
            else:
                self.forward(line_length)
                distance_traveled += line_length
            i += 1

        self.forward(first_and_last_line_length)
        return [self.xcor(), self.ycor()]

    def forward_and_reset(self, distance, draw=True):
        def _forward_and_reset(tur, distance):
            starting_point = tur.position()
            tur.forward(distance)
            arriving_point = (tur.xcor(), tur.ycor())
            tur.teleport(starting_point[0], starting_point[1])
            return arriving_point

        if not draw:
            return self.without_drawing(_forward_and_reset, {"distance": distance})
        return _forward_and_reset(self, distance)

    def calculate_circle_center(self, radius):
        original_heading = self.heading()
        self.setheading(self.heading() + 90)
        circle_center = self.forward_and_reset(radius, False)
        self.setheading(original_heading)
        return circle_center

    def circle_and_return_center(self, radius, extent=None, steps=None):
        circle_center = self.calculate_circle_center(radius)
        if extent is not None or steps is not None:
            self.circle(radius, extent, steps)
        else:
            self.circle(radius)
        return circle_center

    def polygon_centered_at_turtle(self, radius, edges=5, starting_angle=0, draw_radii=False):
        def draw_polygon_centered_at_turtle(tur, radius, edges, starting_angle, draw_radii):
            angle = 360 / edges
            center = tur.pos()
            vertices = []

            tur.setheading(starting_angle)

            for _ in range(edges):
                tur.forward_optional_draw(radius, draw_radii)
                vertices.append(tur.pos())
                tur.teleport(center)
                tur.left(angle)

            for i in range(edges):
                tur.teleport(vertices[i])
                tur.goto(vertices[(i+1)%edges])

            return vertices

        return self.invariant_draw(
            draw_polygon_centered_at_turtle,
            {"radius": radius, "edges": edges, "starting_angle": starting_angle, "draw_radii": draw_radii},
        )        

    def circle_centered_at_turtle(self, radius, extent=None, steps=None):
        def draw_circle_centered_at_turtle(tur, radius, extent=None, steps=None):
            tur.setheading(0)
            tur.teleport(tur.xcor(), tur.ycor() - radius)
            if extent is not None or steps is not None:
                tur.circle(radius, extent, steps)
            else:
                tur.circle(radius)

        return self.invariant_draw(
            draw_circle_centered_at_turtle,
            {"radius": radius, "extent": extent, "steps": steps},
        )

    def stepped_circle_centered_at_turtle(self, radius, number_of_steps):
        def stepped_circle(tur, radius, number_of_steps):
            angle = 360 / number_of_steps
            steps = []

            self.setheading(0)
            self.teleport(self.xcor(), self.ycor() - radius)

            for i in range(number_of_steps):
                self.circle(radius, extent=angle)
                steps.append(self.position())
            
            return steps

        return self.invariant_draw(
            stepped_circle,
            {"radius": radius, "number_of_steps": number_of_steps},
        )

    def quadratic_bezier(self, start, control, end, steps=80, move_to_start=True):
        x0, y0 = start
        x1, y1 = control
        x2, y2 = end

        if steps <= 0:
            steps = 1

        points = []

        if move_to_start:
            self.teleport(x0, y0)
        else:
            self.goto(x0, y0)

        for i in range(1, steps + 1):
            t = i / steps
            mt = 1 - t
            x = (mt * mt * x0) + (2 * mt * t * x1) + (t * t * x2)
            y = (mt * mt * y0) + (2 * mt * t * y1) + (t * t * y2)
            self.goto(x, y)
            points.append((x, y))

        return points

    def cubic_bezier(
        self, start, control1, control2, end, steps=80, move_to_start=True
    ):
        x0, y0 = start
        x1, y1 = control1
        x2, y2 = control2
        x3, y3 = end

        if steps <= 0:
            steps = 1

        points = []

        if move_to_start:
            self.teleport(x0, y0)
        else:
            self.goto(x0, y0)

        for i in range(1, steps + 1):
            t = i / steps
            mt = 1 - t
            x = (
                (mt * mt * mt * x0)
                + (3 * mt * mt * t * x1)
                + (3 * mt * t * t * x2)
                + (t * t * t * x3)
            )
            y = (
                (mt * mt * mt * y0)
                + (3 * mt * mt * t * y1)
                + (3 * mt * t * t * y2)
                + (t * t * t * y3)
            )
            self.goto(x, y)
            points.append((x, y))

        return points
    # endregion