import numpy as np
from numpy.ctypeslib import ndpointer 
from PIL import Image
import requests
from io import BytesIO

from framebuffer import * 

lib.init_buffer()

response = requests.get("https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png")
img = Image.open(BytesIO(response.content))
#img = Image.open("images/demo1.png")
image_array = np.array(img, dtype=np.dtype('u1'))
h, w, _ = image_array.shape
image_array = image_array.ravel()
#lib.draw_rect(0,0,w,h,255,255,255)
lib.set_buffer2d(np.random.randint(1024 - w), np.random.randint(768 - h), w, h, image_array)

lib.close_buffer()