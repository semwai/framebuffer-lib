import time 
import types
import os   

from framebuffer.mouse import Mouse
from framebuffer.framebuffer import Framebuffer
from framebuffer.fb_string import FB_Writer

def pin(point, rect):
    """
    is point inside rectange
    """
    (x, y) = point
    (x1, y1, x2, y2) = rect 
    if x1 < x and x < x2:
        if y1 < y and y < y2:
            return True
    return False


class MyApp(Mouse):
    
    bw = 46
    bh = 46
    border = 10
    margin = 5
    background = 125, 50, 50
    color = 230, 230, 230
    textColor = 64, 64 ,64, 255
    btns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', '<', '>']
    text = ''
     

    def btn_rect(self, number):
        x = self.border * (number+1) + self.bw * number
        y = self.border
        return x, y, x + self.bw, y + self.bh

    def __init__(self):
        self.fb = Framebuffer()
        self.fb.clear_screen()
        self.txt = FB_Writer(size = self.bh//2, color=self.textColor)

        for i in range(0, len(self.btns)):
            x, y, _, _ = self.btn_rect(i)
            fb.draw_rect(start=(x, y), size=(self.bw, self.bh), color=self.background)
            fb.draw_rect(start=(x + self.margin, y + self.margin), size=(self.bw - self.margin*2, self.bh - self.margin*2), color=self.color)
            self.txt.print(self.btns[i], x + self.bw //3 , y + self.bh // 4)

    def onLeftClick(self, x, y):
        w = FB_Writer(size=self.bh//2) 
        f = Framebuffer()
        for i in range(0, 16):
            if pin((x, y), rect=self.btn_rect(self, i)):
                self.text += self.btns[i]
                f.draw_rect(start=(10, 100), size=(900, 50), color=(0, 0, 0))
                w.print(self.text, 10, 100)

        if pin((x, y), rect=self.btn_rect(self, 16)):
            self.text = self.text[:-1] 
            f.draw_rect(start=(10, 100), size=(900, 50), color=(0, 0, 0))
            w.print(self.text, 10, 100)





if __name__ == '__main__':
    fb = Framebuffer()
    app = MyApp()
    time.sleep(999)