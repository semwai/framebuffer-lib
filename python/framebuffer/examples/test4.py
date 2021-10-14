import numpy as np
from numpy.ctypeslib import ndpointer 
from PIL import Image
import requests
from io import BytesIO
import sys

from framebuffer.framebuffer import Framebuffer

fb = Framebuffer()

response = requests.get("https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png")
img = Image.open(BytesIO(response.content))
image_array = np.array(img, dtype=np.dtype('u1'))
h, w, _ = image_array.shape

fb.set_buffer2d(
    start=(np.random.randint(1024 - w), np.random.randint(768 - h)), 
    size=(w, h), 
    buffer=image_array.ravel())

 