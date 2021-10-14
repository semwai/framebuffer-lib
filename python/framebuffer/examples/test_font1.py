from framebuffer.fb_string import FB_Writer
from framebuffer.framebuffer import Framebuffer

fb = Framebuffer()
fb.clear_screen()

writer = FB_Writer(size=50)
writer.print("HELLO", 350, 50)
writer.print("   WORLD", 350, 100)