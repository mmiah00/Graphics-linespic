pixels = []
pic = open ("linepic.ppm", "w")
pic.write ("P3 500 500 255 ")

def initialize (background_color):
    for y in range (500):
        for x in range (500):
            pixels [y] = {background_color.split (" ")}

def plot (x, y, color):
    pixels[y] = color.split (" ")

def line (x1, y1, x2, y2, color):
    x,y = x1, y1
    A = y2 - y1
    B = -1 * (x2 - x1)
    d = 2A + B
    while x < x1:
        plot (x,y)
        if d > 0:
            y = y + 1
            d = d + 2B
        x = x + 1
        d = d + 2A
