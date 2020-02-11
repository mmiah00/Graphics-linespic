from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1 - x0 != 0:
        slope = ((y1 - y0) / (x1 - x0)) + 0.0
        if (slope > 0) & (slope < 1):
            octant1 (x0, y0, x1, y1, screen, color)
        elif slope > 1:
            octant2 (x0, y0, x1, y1, screen, color)
        elif slope < -1:
            octant3 (x1, y1, x0, y0, screen, color)
        elif (slope < 0) & (slope > -1):
            octant4 (x1, y1, x0, y0, screen, color)

def octant1 (x0, y0, x1, y1, screen, color): #also for octant 5
    x,y = x0, y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2*A + B
    while x < x1:
        plot (screen, color, x, y)
        if d > 0:
            y = y + 1
            d = d + 2*B
        x = x + 1
        d = d + 2*A

def octant2 (x0, y0, x1, y1, screen, color): #also for octant 6
    x,y = x0, y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2*A + B
    while x < x1:
        plot (screen, color, x, y)
        if d > 0:
            x = x + 1
            d = d + 2*A
        y = y + 1
        d = d + 2*B

def octant3 (x0, y0, x1, y1, screen, color): #also for octant 7
    x,y = x0, y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = A - 2*B
    while y >= y1:
        plot (screen, color, x, y)
        if d > 0:
            x = x + 1
            d = d + 2*A
        y = y - 1
        d = d + 2*B

def octant4 (x0, y0, x1, y1, screen, color): #also for octant 8
    x,y = x0, y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2*A - B
    while x >= x1:
        plot (screen, color, x, y)
        if d < 0:
            y = y - 1
            d = d - 2*B
        x = x + 1
        d = d + 2*A
