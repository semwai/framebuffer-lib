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

            int position = ((i - y1)*w + (j - x1))*4;
            out[position] = *(fbp + location);
            out[position + 1] = *(fbp + location + 1);
            out[position + 2] = *(fbp + location + 2);
            out[position + 3] = *(fbp + location + 3);
        }
}

void set_buffer2d(int x1, int y1, int w, int h, unsigned char* in) {
    int i, j, k;
    for (i = y1; i < y1 + h; i++)
        for (j = x1; j < x1 + w; j++) {
            location = (j+vinfo.xoffset) * (vinfo.bits_per_pixel/8) + (i+vinfo.yoffset) * finfo.line_length;
             
            int position = ((i - y1)*w + (j - x1))*4;
            int transparency = in[position + 3];
            float tr = (transparency/255.0);
            float ntr = 1 - tr;
            for (k = 0; k < 3; k++)
                *(fbp + location + k) = (char)(tr*in[position + k]+ ntr* *(fbp + location + k));     
             
            *(fbp + location + 3) = 0; 
        }
}
