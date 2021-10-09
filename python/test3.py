from ctypes import *
from time import sleep
import math
import numpy as np
from numpy.ctypeslib import ndpointer 


lib = CDLL("../out/framebuffer-lib.so")
lib.init_buffer()





lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.uintp, ndim=1, flags='C') ]
def get_buffer2d(x1: int, y1: int, x2: int, y2: int, np2d_int_arr):
    xpp = (np2d_int_arr.__array_interface__['data'][0] 
      + np.arange(np2d_int_arr.shape[0])*x.strides[0]).astype(np.uintp) 
    return lib.get_buffer2d(0,0,2,2,xpp)


x = np.array([[0, 0], [0, 0]], dtype=np.int32)
print(x)
get_buffer2d(0, 0, 1, 1, x)
print(x)

lib.close_buffer()