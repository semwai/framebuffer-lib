from framebuffer import * 
import asyncio
import numpy as np
import time 
import ctypes
lib.init_buffer()

lib.draw_sphere(300, 300, 300, *[np.random.randint(256) for i in range(3)])

cl = False

def mouse_move(x, y):
    global cl
    if cl:
        lib.draw_sphere(x, y, 30, *[np.random.randint(256) for i in range(3)])

def click(x, y):
    global cl
    cl = ~cl


ftype = ctypes.CFUNCTYPE(None, c_int, c_int)

lib.mouse_poll(ftype(mouse_move), ftype(click), ftype(click), ftype(click))
time.sleep(15)


lib.close_buffer()

 
 