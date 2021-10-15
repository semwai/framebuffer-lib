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
            self.__lib.mouse_poll.argtypes = [py_object, 
                CFUNCTYPE(None, py_object, c_int, c_int), 
                CFUNCTYPE(None, py_object, c_int, c_int), 
                CFUNCTYPE(None, py_object, c_int, c_int), 
                CFUNCTYPE(None, py_object, c_int, c_int)]

            self.__lib.init_buffer()
        return self.instance
    
    def __del__(self):
        self.__lib.close_buffer()
        print('close buffer\n')

    def draw_rect(self, start=(0, 0), size=(100, 100), color=(255, 255, 255)):
        self.__lib.draw_rect(start[0], start[1], size[0], size[1], color[0], color[1], color[2])

    def draw_sphere(self, center=(100, 100), radious=25, color=(255, 255, 255)):
        self.__lib.draw_sphere(center[0], center[1], radious, color[0], color[1], color[2])

    def draw_circle(self, center=(100, 100), radious=(15, 25), color=(255, 255, 255)):
        """ 
        circle with border = rad[1] - rad[0]
        """
        self.__lib.draw_circle(center[0], center[1], radious[0], radious[1], color[0], color[1], color[2])

    def clear_screen(self):
        self.__lib.clear_screen()
    
    def get_buffer2d(self, start=(0, 0), size=(0, 0), buffer=np.array([], dtype=np.dtype('u1'))):
        self.__lib.get_buffer2d(start[0], start[1], size[0], size[1], buffer)

    def set_buffer2d(self, start=(0, 0), size=(0, 0), buffer=np.array([], dtype=np.dtype('u1'))):
        self.__lib.set_buffer2d(start[0], start[1], size[0], size[1], buffer)

    def set_mouse_poll(self, sender, move, left_click, middle_click, right_click):
        ftype = CFUNCTYPE(None, py_object, c_int, c_int)
        self.__lib.mouse_poll(sender, ftype(move), ftype(left_click), ftype(middle_click), ftype(right_click))