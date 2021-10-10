from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer 
# `make lib` required
lib = CDLL("../out/framebuffer-lib.so")

lib.init_buffer.argtypes = []
lib.close_buffer.argtypes = []

lib.draw_rect.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
lib.draw_sphere.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int]
lib.draw_circle.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
lib.clear_screen.argtypes = []
lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('i1'), flags='C') ]
lib.set_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('i1'), flags='C') ]

lib.mouse_poll.argtypes = [CFUNCTYPE(None, c_int, c_int)]