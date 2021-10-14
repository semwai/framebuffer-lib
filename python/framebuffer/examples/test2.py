from ctypes import *
#import asyncio
from time import sleep
import math

from framebuffer.framebuffer import Framebuffer

fb = Framebuffer()

x, y = 512, 384
for i in range(360):
    fb.draw_circle(center=(x, y), radious=(30, 50), color=(0, 0, 0))
    
    x = int(512 + 100*math.cos(math.radians(i)))
    y = int(384 + 100*math.sin(math.radians(i)))
    lib.draw_circle(x, y, 30, 50, 50, i, 50)
    sleep(0.01)

lib.clear_screen()
lib.close_buffer()