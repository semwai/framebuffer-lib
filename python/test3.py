from ctypes import *
from time import sleep
import math
import numpy as np
from numpy.ctypeslib import ndpointer 


lib = CDLL("../out/framebuffer-lib.so")
lib.init_buffer()


lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.uintp, ndim=1, flags='C') ]
def get_buffer2d(x1: int, y1: int, w: int, h: int, np2d_int_arr):
    xpp = (np2d_int_arr.__array_interface__['data'][0] 
      + np.arange(np2d_int_arr.shape[0])*np2d_int_arr.strides[0]).astype(np.uintp) 
    return lib.get_buffer2d(x1,y1,w,h,xpp)

lib.set_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.uintp, flags='C') ]
def set_buffer2d(x1: int, y1: int, w: int, h: int, np2d_int_arr):
    return lib.set_buffer2d(x1,y1,w,h,np2d_int_arr)

#w,h = 100, 100
#x1, y1 = 25, 25
#x = np.zeros((w,h), dtype=np.uint8)
#get_buffer2d(x1, y1, x1 + w, y1 + h, x)
lib.clear_screen()
y = np.zeros((512*384*3), dtype=np.uint)
y[0::3] = 0
y[1::3] = 25
y[2::3] = 0
y[192*512+256] = 255
#for i in range(0, 384):
#    for j in range(0, 512):  
#        y[i*512 + j*3    ] = 255
#        y[i*512 + j*3 + 1] = 0
#        y[i*512 + j*3 + 2] = 0

for i in range(100):
    lib.set_buffer2d(i, i, 512, 384, y)
    sleep(0.05)
     

#x = np.zeros((3,3*3), dtype=np.uint8)
#x[::,::2]=255
#print(x)
#set_buffer2d(0, 0, 3, 3, x)



lib.close_buffer()