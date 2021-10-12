import numpy as np
#from numpy.ctypeslib import ndpointer 

from framebuffer import * 

lib.init_buffer()
#lib.draw_rect(0, 0, 1024, 768, 192, 192, 192)

w, h = 500, 500
data = np.array([0, 0, 127, 127] * (w * h), dtype=np.dtype('u1'))
#x, y = np.random.randint(1024 - w), np.random.randint(768 - h)
x, y = 0, 0
lib.set_buffer2d(x, y, w, h, data)

lib.close_buffer() 