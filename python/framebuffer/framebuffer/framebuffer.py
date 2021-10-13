from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer 


import importlib_resources

my_resources = importlib_resources.files("framebuffer")
library = (my_resources / "framebuffer-lib.so") 

# `make lib` required
lib = CDLL(library)

lib.init_buffer.argtypes = []
lib.close_buffer.argtypes = []

lib.draw_rect.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
lib.draw_sphere.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int]
lib.draw_circle.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
lib.clear_screen.argtypes = []
lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('u1'), flags='C') ]
lib.set_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('u1'), flags='C') ]

lib.mouse_poll.argtypes = [CFUNCTYPE(None, c_int, c_int)]

def init_buffer():
    global lib
    lib.init_buffer()