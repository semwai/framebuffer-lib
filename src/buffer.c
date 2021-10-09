#include <stdlib.h>
#include <stdio.h>
#include <linux/fb.h>

extern struct fb_var_screeninfo vinfo;
extern struct fb_fix_screeninfo finfo;
extern char *fbp;
extern long int location;

void get_buffer2d(int x1, int y1, int w, int h, char* out[]) {
    int i, j;
    for (i = y1; i < h; i++)
        for (j = x1; j < w; j++) {
            location = (j+vinfo.xoffset) * (vinfo.bits_per_pixel/8) +
                (i+vinfo.yoffset) * finfo.line_length;

            out[i - y1][j - x1] = *(fbp + location);
            out[i - y1][j - x1 + 1] = *(fbp + location + 1);
            out[i - y1][j - x1 + 2] = *(fbp + location + 2);
        }
}

void set_buffer2d(int x1, int y1, int w, int h, long* in) {
    int i, j;
    int k = 0;
    for (i = y1; i < y1+h; i++)
        for (j = x1*3; j < (x1+w)*3; j+= 3) {
            location = (j/3+vinfo.xoffset) * (vinfo.bits_per_pixel/8) + (i+vinfo.yoffset) * finfo.line_length;
            //k += 1;
            int delta = i % 3;

            *(fbp + location + 0) = in[(i - y1)*w+(j - x1) + delta + 0];     
            *(fbp + location + 1) = in[(i - y1)*w+(j - x1) + delta + 1];
            *(fbp + location + 2) = in[(i - y1)*w+(j - x1) + delta + 2];
            //*(fbp + location + 3) = 0;
        }
}
