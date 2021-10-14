from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer 
import importlib_resources


class Framebuffer(object):
    

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Framebuffer, self).__new__(self)

            # `make lib` required
            my_resources = importlib_resources.files("framebuffer")
            library = (my_resources / "framebuffer-lib.so") 
            self.__lib = CDLL(library)
            self.__lib.init_buffer.argtypes = []
            self.__lib.close_buffer.argtypes = []
            self.__lib.draw_rect.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
            self.__lib.draw_sphere.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int]
            self.__lib.draw_circle.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int]
            self.__lib.clear_screen.argtypes = []
            self.__lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('u1'), flags='C') ]
            self.__lib.set_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('u1'), flags='C') ]
            self.__lib.mouse_poll.argtypes = [CFUNCTYPE(None, c_int, c_int)]

            self.__lib.init_buffer()
        return self.instance
    
    def __del__(self):
        self.__lib.close_buffer()
        print('close buffer\n')

    def draw_rect(self, start=(0, 0), size=(100, 100), color=(255, 255, 255)):
        self.__lib.draw_rect(start[0], start[1], size[0], size[1], color[0], color[1], color[2])