from libs.utils import rotate_point

def lorenz_attractor(x, y, z, sigma, beta, rho, dt):
    """
    Returns x, y, z coordinates of the Lorenz attractor after one time step
    
    :param x: x coordinate
    :param y: y coordinate 
    :param z: z coordinate
    :param sigma: sigma parameter of the Lorenz attractor
    :param beta: beta parameter of the Lorenz attractor
    :param rho: rho parameter of the Lorenz attractor
    :param dt: time step

    :return: returns a tuple (x, y, z) after one time step
    """
    dx = (sigma * (y - x)) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt

    x += dx
    y += dy
    z += dz

    return x, y, z

def rossler_attractor(x, y, z, a, b, c, dt):
    """
    Returns x, y, z coordinates of the Rossler attractor after one time step
    
    :param x: x coordinate
    :param y: y coordinate 
    :param z: z coordinate
    :param sigma: sigma parameter of the Lorenz attractor
    :param beta: beta parameter of the Lorenz attractor
    :param rho: rho parameter of the Lorenz attractor
    :param dt: time step
    
    :return: returns a tuple (x, y, z) after one time step
    """
    dx = (-y - z) * dt
    dy = (x + a*y) * dt
    dz = (b + z*(x-c)) * dt

    x += dx
    y += dy
    z += dz

    return x, y, z

def draw_attractor(tur, attractor_method, attractor_parameters, time_steps=20000, scale_factor=10, rotation_angles=None, number_of_steps_to_skip=0):
    """
    Draws an attractor using the specified method and parameters.
    
    :param tur: SvgTurtle instance for drawing
    :param attractor_method: function to compute the next point of the attractor
    :param attractor_parameters: tuple of parameters for the attractor method
    :param time_steps: number of iterations to draw
    :param scale_factor: scaling factor for the coordinates
    :param rotation_angles: angles for rotating the points
    """

    if number_of_steps_to_skip > 0:
        tur.penup()
    for i in range(time_steps):
        if (i > number_of_steps_to_skip and not tur.isdown()):
            tur.pendown()
        x, y, z = attractor_method(**attractor_parameters)
        attractor_parameters['x'] = x
        attractor_parameters['y'] = y
        attractor_parameters['z'] = z
        if rotation_angles:
            print("rotating angles?")
            x1, y1 = rotate_point(x, y, z, rotation_angles[0], rotation_angles[1])
        else:
            x1, y1 = x, y
        tur.goto(x1*scale_factor, y1*scale_factor)
    
    return tur
