from display import *
from draw import *
import random 

s = new_screen()
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]


#draw_line (250, 250, 250, 300, s, YELLOW)
#draw_line (250, 300, 300,300, s, YELLOW)
#draw_line (300, 300, 300, 250, s, YELLOW)
#draw_line (300, 250, 250, 250, s, YELLOW)

def square (x,y, length, color): 
	x0 = x - (length/2)
	y0 = y - (length/2)
	draw_line (x0, y0, x0 + length, y0, s, color)
	draw_line (x0 + length, y0, x0 + length, y0 + length, s, color)
	draw_line (x0 + length, y0 + length, x0, y0 + length,s,color)
	draw_line (x0, y0 + length, x0,y0,s,color)

size = 25
color = 10
while (size < 450):
	square (250,250,size,[255,255,color])
	color += 50 
	size += 25

display(s)
save_ppm(s, 'binary2.ppm')
save_ppm_ascii(s, 'ascii2.ppm')
save_extension(s, 'drawing.png')
