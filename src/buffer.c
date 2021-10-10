#include <stdlib.h>
#include <stdio.h>
#include <linux/fb.h>

extern struct fb_var_screeninfo vinfo;
extern struct fb_fix_screeninfo finfo;
extern char *fbp;
extern long int location;

void get_buffer2d(int x1, int y1, int w, int h, unsigned char* out) {
    int i, j;
    for (i = y1; i < y1 + h; i++)
        for (j = x1; j < x1 + w; j++) {
            location = (j+vinfo.xoffset) * (vinfo.bits_per_pixel/8) +
                (i+vinfo.yoffset) * finfo.line_length;

            int position = ((i - y1)*w + (j - x1))*3;
            out[position] = *(fbp + location);
            out[position + 1] = *(fbp + location + 1);
            out[position + 2] = *(fbp + location + 2);
        }
}

void set_buffer2d(int x1, int y1, int w, int h, unsigned char* in) {
    int i, j;
    for (i = y1; i < y1 + h; i++)
        for (j = x1; j < x1 + w; j++) {
            location = (j+vinfo.xoffset) * (vinfo.bits_per_pixel/8) + (i+vinfo.yoffset) * finfo.line_length;
             
            int position = ((i - y1)*w + (j - x1))*3;
            *(fbp + location + 0) = in[position];     
            *(fbp + location + 1) = in[position + 1];
            *(fbp + location + 2) = in[position + 2];
            //*(fbp + location + 3) = 0;
        }
}
