#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>
#include <linux/fb.h>
#include <sys/mman.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include "init.h"

struct fb_var_screeninfo vinfo;
struct fb_fix_screeninfo finfo;
long int screensize;
char *fbp;
long int location;
int fbfd;


int init_buffer(){
    fbfd = open("/dev/fb0", O_RDWR);
    if (fbfd == -1) {
        perror("opening /dev/fb0");
        return -1;
    }
    // Get fixed screen information
    if (ioctl(fbfd, FBIOGET_FSCREENINFO, &finfo)) {
        printf("Error reading fixed information.\n");
        return -2;
    }
    // Get variable screen information
    if (ioctl(fbfd, FBIOGET_VSCREENINFO, &vinfo)) {
        printf("Error reading variable information.\n");
        return -3;
    }
    printf("%dx%d, %dbpp\n", vinfo.xres, vinfo.yres, vinfo.bits_per_pixel );
    // Figure out the size of the screen in bytes
    screensize = vinfo.xres * vinfo.yres * vinfo.bits_per_pixel / 8;
    // Map the device to memory
    fbp = (char *)mmap(0, screensize, PROT_READ | PROT_WRITE, MAP_SHARED, fbfd, 0);
    if (*fbp == -1) {
        printf("Error: failed to map framebuffer device to memory.\n");
        return -4;
    }
    printf("The framebuffer device was mapped to memory successfully.\n");
    return 0;
}

void close_buffer(){
    munmap(fbp, screensize);
    close(fbfd);
}

unsigned int get_screen_width(){
    return vinfo.xres;
}

unsigned int get_screen_height(){
    return vinfo.yres;
}