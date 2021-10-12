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
            out[position + 0] = *(fbp + location + 2);
            out[position + 1] = *(fbp + location + 1);
            out[position + 2] = *(fbp + location + 0);
            out[position + 3] = *(fbp + location + 3);
        }
}

void set_buffer2d(int x1, int y1, int w, int h, unsigned char* in) {
    int i, j, k;
    for (i = y1; i < y1 + h; i++)
        for (j = x1; j < x1 + w; j++) {
            location = (j+vinfo.xoffset) * (vinfo.bits_per_pixel/8) + (i+vinfo.yoffset) * finfo.line_length;
            int position = ((i - y1)*w + (j - x1))*4;
            float tr = in[position + 3]/255.0;
            for (k = 0; k < 3; k++){
                unsigned char *loc = fbp + location + 2 - k;
                float new_color = tr*(in[position + k]/255.0) + (1.0 - tr) * (*loc/255.0);
                *loc = (unsigned char)(new_color*255.0);
            }
            *(fbp + location + 3) = 255; 
        }
}
