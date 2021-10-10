from ctypes import *
from time import sleep
import math
import numpy as np
from numpy.ctypeslib import ndpointer 
from PIL import Image
import requests
from io import BytesIO

lib = CDLL("../out/framebuffer-lib.so")
lib.init_buffer()

lib.get_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('i1'), flags='C') ]
lib.set_buffer2d.argtypes = [c_int, c_int, c_int, c_int, ndpointer(dtype=np.dtype('i1'), flags='C') ]


response = requests.get("https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png")
img = Image.open(BytesIO(response.content))
image_array = np.array(img, dtype=np.dtype('i1')).flatten()
#image_array = np.array([image_array[i] for i in range(image_array.shape[0]) if i % 4 != 3], dtype=np.dtype('i1'))
#lib.clear_screen()
lib.set_buffer2d(0, 0, 800, 600, image_array)
lib.close_buffer()