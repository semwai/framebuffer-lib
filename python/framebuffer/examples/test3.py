from ctypes import *
from time import sleep
import math
import numpy as np
from numpy.ctypeslib import ndpointer 


from framebuffer.framebuffer import Framebuffer

fb = Framebuffer()
fb.clear_screen()
y = np.zeros((512*384*4), dtype=np.dtype('u1'))
y[0::4] = 255
y[1::4] = 0
y[2::4] = 0
y[3::4] = 255 #alpha
y[(192*512+256)*3] = 0
 

for i in range(100):
    fb.set_buffer2d(start=(i, i), size=(512, 384), buffer=y)


z = np.zeros((612*484*4), dtype=np.dtype('u1'))
fb.get_buffer2d(start=(0, 0), size=(612, 484), buffer=z)
fb.set_buffer2d(start=(100, 0), size=(612, 484), buffer=z)
