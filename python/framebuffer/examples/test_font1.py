from framebuffer import *
from framebuffer_font import char_to_pixels, draw_text

lib.init_buffer()

#lib.clear_screen()
color = (255, 255, 255, 192)
draw_text("ABC", 0, 0, 40, color=color)
draw_text("Hello to /dev/fb0", 0, 40, 40, color=color)
lib.close_buffer()