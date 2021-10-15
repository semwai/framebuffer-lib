#include <linux/fb.h>
#include "figures.h"

extern struct fb_var_screeninfo vinfo;
extern struct fb_fix_screeninfo finfo;
extern char *fbp;
extern long int location;


void draw_rect(int x1, int y1, int w, int h, int r, int g, int b){
    for (int y = y1; y < y1 + h; y++ ) {
    	for (int x = x1; x < x1 + w; x++ ) {
            location = (x+vinfo.xoffset) * (vinfo.bits_per_pixel/8) +
                (y+vinfo.yoffset) * finfo.line_length;
            if ( vinfo.bits_per_pixel == 32 ) {
                *(fbp + location) = b;         
                *(fbp + location + 1) = g;     
                *(fbp + location + 2) = r;     
                *(fbp + location + 3) = 0;  // No transparency
            } else  { //assume 16bpp 
                unsigned short int t = r<<11 | g << 5 | b;
                *((unsigned short int*)(fbp + location)) = t;
            }      
        }
    }
}

void draw_sphere(int x1, int y1, int rad, int r, int g, int b) {
    for (int y = y1 - rad; y < y1 + rad; y++ ) {
    	for (int x = x1 - rad; x < x1 + rad; x++ ) {
            int eq = (x - x1)*(x - x1) + (y - y1)*(y - y1);
            if (eq> rad*rad) continue;

            location = (x+vinfo.xoffset) * (vinfo.bits_per_pixel/8) +
                (y+vinfo.yoffset) * finfo.line_length;
            if ( vinfo.bits_per_pixel == 32 ) {
                *(fbp + location) = b;         
                *(fbp + location + 1) = g;     
                *(fbp + location + 2) = r;     
                *(fbp + location + 3) = 0;  // No transparency
            } else  { //assume 16bpp 
                unsigned short int t = r<<11 | g << 5 | b;
                *((unsigned short int*)(fbp + location)) = t;
            }      
        }
    }
}


void draw_circle(int x1, int y1, int radin, int radout, int r, int g, int b) {
    for (int y = y1 - radout; y < y1 + radout; y++ ) {
    	for (int x = x1 - radout; x < x1 + radout; x++ ) {
            int eq = (x - x1)*(x - x1) + (y - y1)*(y - y1);
            if (eq>radout*radout||eq<radin*radin)
                continue;

            location = (x+vinfo.xoffset) * (vinfo.bits_per_pixel/8) +
                (y+vinfo.yoffset) * finfo.line_length;
            if ( vinfo.bits_per_pixel == 32 ) {
                *(fbp + location) = b;         
                *(fbp + location + 1) = g;     
                *(fbp + location + 2) = r;     
                *(fbp + location + 3) = 0;  // No transparency
            } else  { //assume 16bpp 
                unsigned short int t = r<<11 | g << 5 | b;
                *((unsigned short int*)(fbp + location)) = t;
            }      
        }
    }
}

void clear_screen(){
    draw_rect(0, 0, vinfo.xres, vinfo.yres, 0, 0, 0);
}