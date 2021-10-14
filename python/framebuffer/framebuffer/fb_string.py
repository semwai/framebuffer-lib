from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

from framebuffer.framebuffer import Framebuffer


class FB_Writer(object):
    
    def __init__(self, font='fonts/JetBrainsMono-Medium.ttf', size=14, color=(255, 255, 255, 255)):
        self.font = font
        self.size = size
        self.color = color
        self.__fb = Framebuffer()

    def str_to_pixels(self, ch):
        """
        Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
        """
        font = ImageFont.truetype(self.font, self.size) 
        w, h = font.getsize(ch)  
        h *= 2
        image = Image.new('L', (w, h), 1)  
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), ch, font=font) 
        arr = np.asarray(image)
        arr = np.where(arr, 0, 1)   
        arr = arr[(arr != 0).any(axis=1)]
        return arr

    def print(self, input, x, y):
        """
        Draw text and return width & height
        """
        c = self.str_to_pixels(input)
        h,w = c.shape
        c = np.array([[self.color[0]*e, self.color[1]*e, self.color[2]*e, self.color[3]*e] for e in c.ravel()]).ravel().astype(dtype=np.dtype('u1'))
        self.__fb.set_buffer2d(start=(x, y), size=(w, h), buffer=c)
        return w,h