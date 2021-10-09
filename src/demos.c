#include <linux/fb.h>
#include <unistd.h>
#include "demos.h"
#include "figures.h"

extern struct fb_var_screeninfo vinfo;
extern struct fb_fix_screeninfo finfo;
extern char *fbp;
extern long int location;

void demo1(){
    clear_screen();
    int x = 0, y = 0;
    int i = 0;
    // Figure out where in memory to put the pixel
    draw_rect(100, 100, 924, 200, 0, 255, 0);
    draw_rect(100, 200, 200, 668, 255, 255, 0);
    draw_rect(824, 200, 924, 668, 0, 255, 255);
    draw_rect(200, 568, 824, 668, 255, 0, 255);
    for (i = 0; i < 1000; i++){
        usleep(1000 * 10);
        for (y = 200; y < 568; y++ ) {
            for ( x = 200; x < 824; x++ ) {
                location = (x+vinfo.xoffset) * (vinfo.bits_per_pixel/8) + 
                    (y+vinfo.yoffset) * finfo.line_length;
                int r = i * 10;
                int g = y + i;
                int b = (x + i) * (y);
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
}

void demo2(){
    clear_screen();
    draw_rect(0, 0, 1024, 768, 90, 60, 0);
    draw_sphere(300, 300, 150, 255, 255, 0);
    draw_circle(400, 320, 100, 150, 50, 215, 33);
}

