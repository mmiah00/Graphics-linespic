from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    slope = (y1 - y0) / (x1 - x0) + 0.0
    if slope > 0 & slope < 1:
        octant1 (x0, y0, x1, y1, color)
    elif slope

def octant1 (x0, y0, x1, y1, color):
    x,y = x1, y1
    A = y2 - y1
    B = -1 * (x2 - x1)
    d = 2*A + B
    while x < x1:
        plot (x,y, color)
        if d > 0:
            y = y + 1
            d = d + 2*B
        x = x + 1
        d = d + 2*A
