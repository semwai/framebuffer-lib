import numpy as np
from framebuffer.framebuffer import Framebuffer

fb = Framebuffer()
start = 0, 0
size = 500, 500
color = 255, 0, 0
fb.draw_rect(start=start, size=size, color=color)
# create 'second' object, but it is a singleton
fb2 = Framebuffer()
fb2.draw_rect(start=(100, 100), size=(250, 250), color=(255, 255, 255))