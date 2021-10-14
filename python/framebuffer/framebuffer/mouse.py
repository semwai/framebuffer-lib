import ctypes
from enum import Enum
from framebuffer.framebuffer import Framebuffer

class Mouse(object):
    """
    Mouse event handler
    """
    def onMove(self, x, y):
        pass

    def onLeftClick(self, x, y):
        print('old')
        pass

    def onMiddleClick(self, x, y):
        pass

    def onRightClick(self, x, y):
        pass
 

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Mouse, self).__new__(self)

        self.__fb = Framebuffer()
        ftype = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.c_int, ctypes.c_int)
        self.__fb.set_mouse_poll(self, ftype(self.onMove), ftype(self.onLeftClick), ftype(self.onMiddleClick), ftype(self.onRightClick))
        return self.instance