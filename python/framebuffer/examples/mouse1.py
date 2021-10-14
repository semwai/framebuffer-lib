import time 
import types

from framebuffer.mouse import Mouse
from framebuffer.framebuffer import Framebuffer

fb = Framebuffer()

class AppMouse(Mouse):
    def onLeftClick(self, x, y):
        print(x ,y)
        fb.draw_circle(center=(x, y), radious=(15, 25), color=(255, 255, 255, 255))
 
mouse = AppMouse()
time.sleep(10)