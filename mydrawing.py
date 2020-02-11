from display import *
from draw import *
import random 

s = new_screen()
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]

def rect (x1, y1, x2, y2, length, color):
    a,b,c,d = x1, y1, x2, y2
    delta_x = x2 - x1
    delta_y = y2 - x1
    for i in range (length):
        draw_line (a,b,c,d, s, color)
        a += delta_x
        b += delta_y
        c += delta_x
        d += delta_y

rect (250,250, 450,450, 100,YELLOW )

draw_line (250, 250, 250, 300, s, YELLOW)
draw_line (250, 300, 300,300, s, YELLOW)
draw_line (300, 300, 300, 250, s, YELLOW)
draw_line (300, 250, 250, 250, s, YELLOW)

display(s)
save_ppm(s, 'binary2.ppm')
save_ppm_ascii(s, 'ascii2.ppm')
save_extension(s, 'drawing.png')
