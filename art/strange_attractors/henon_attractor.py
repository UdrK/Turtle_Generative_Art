import math

angle = 2.41 # rotation angle in radians (try 0.5–1.2 for interesting behavior)
iterations = 10000
transient = 100  # skip initial steps to avoid transients

x, y = 0.01, 0.01

scale = 400  # zoom level

def rotated_henon(x, y, angle):
    try:
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        x_new = x * cos_a - (y - math.pow(x, 2)) * sin_a
        y_new = x * sin_a + (y - math.pow(x, 2)) * cos_a
    except OverflowError:
        return float('inf'), float('inf')  # will be caught by divergence check
    return x_new, y_new

def loop(tur, x, y, screen_width, screen_height):
    points = 0
    min_dist = 20
    last_x, last_y = None, None

    for i in range(iterations):
        x, y = rotated_henon(x, y, angle)

        if abs(x) > 1e6 or abs(y) > 1e6:
            break

        if i > transient and i % 2 == 0:
            screen_x = x * scale
            screen_y = y * scale

            # Only plot if within screen bounds (avoid going off-canvas)
            if abs(screen_x) < screen_width // 2 and abs(screen_y) < screen_height // 2:
                if last_x is None or math.hypot(screen_x - last_x, screen_y - last_y) > min_dist:
                    tur.goto(screen_x, screen_y)
                    tur.dot(1)
                    last_x, last_y = screen_x, screen_y
                    points += 1
        if points > 1000:
            break
