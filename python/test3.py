from ctypes import *
from time import sleep
import math
import numpy as np
from numpy.ctypeslib import ndpointer 


lib = CDLL("../out/framebuffer-lib.so")
lib.init_buffer()


lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('i1'), flags='C') ]
lib.set_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('i1'), flags='C') ]


lib.clear_screen()
y = np.zeros((512*384*3), dtype=np.dtype('i1'))
y[0::3] = 255
y[1::3] = 0
y[2::3] = 0
y[(192*512+256)*3] = 0
 

for i in range(100):
    lib.set_buffer2d(i, i, 512, 384, y)
    #sleep(0.05)


z = np.zeros((612*484*3), dtype=np.dtype('i1'))
lib.get_buffer2d(0, 0, 612, 484, z)
lib.set_buffer2d(100, 0, 612, 484, z)
lib.close_buffer()