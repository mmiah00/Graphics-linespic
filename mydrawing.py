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
# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c)
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);


display(s)
save_ppm(s, 'binary2.ppm')
save_ppm_ascii(s, 'ascii2.ppm')
save_extension(s, 'drawing.png')
