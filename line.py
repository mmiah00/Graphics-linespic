pixels = []
pic = open ("linepic.ppm", "w")
pic.write ("P3 500 500 255 ")

YELLOW = "255 255 0"

def initialize (background_color):
    for y in range (500):
        pixels.append (background_color.split (" "))

initialize (YELLOW)

def plot (x, y, color):
    pixels[y] = color.split (" ")

def line (x1, y1, x2, y2, color):
    x,y = x1, y1
    A = y2 - y1
    B = -1 * (x2 - x1)
    d = 2*A + B
    while x < x1:
        plot (x,y)
        if d > 0:
            y = y + 1
            d = d + 2*B
        x = x + 1
        d = d + 2*A

line (0, 0, 39, 55, YELLOW)

def drawpic ():
    for y in range (500):
        pic.write (pixels[y][0] + " ")
        pic.write (pixels[y][1] + " ")
        pic.write (pixels[y][2] + " ")

drawpic ()
pic.close ()
