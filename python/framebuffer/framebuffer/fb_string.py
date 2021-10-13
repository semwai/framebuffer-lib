from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

from framebuffer import *


def char_to_pixels(ch, path='fonts/JetBrainsMono-Medium.ttf', fontsize=14):
    """
    Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
    """
    font = ImageFont.truetype(path, fontsize) 
    w, h = font.getsize(ch)  
    h *= 2
    image = Image.new('L', (w, h), 1)  
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ch, font=font) 
    arr = np.asarray(image)
    arr = np.where(arr, 0, 1)   
    arr = arr[(arr != 0).any(axis=1)]
    return arr

def draw_text(input, x, y, fontsize=14, font='fonts/JetBrainsMono-Medium.ttf', color=(255, 255, 255, 255)):
    """
    Draw text and return width & height
    """
    c = char_to_pixels(input, fontsize=fontsize)
    h,w = c.shape
    c = np.array([[color[0]*e, color[1]*e, color[2]*e, color[3]*e] for e in c.ravel()]).ravel().astype(dtype=np.dtype('u1'))
    lib.set_buffer2d(x, y, w, h, c)
    return w,h

