from ctypes import *
# `make lib` required
lib = CDLL("../out/framebuffer-lib.so")

lib.init_buffer()

lib.demo2()

lib.draw_rect(500,100,750,150,255,255,255)
lib.draw_rect(500,150,750,200,000,000,255)
lib.draw_rect(500,200,750,250,255,000,000)

lib.close_buffer()