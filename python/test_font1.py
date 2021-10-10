from framebuffer import *
from framebuffer_font import char_to_pixels, draw_text

lib.init_buffer()

lib.clear_screen()
draw_text("ABC", 0, 0, 40)
draw_text("Hello to /dev/fb0", 0, 40, 40)

lib.close_buffer()