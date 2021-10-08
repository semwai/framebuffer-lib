#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/prctl.h>
#include <signal.h>
#include <unistd.h>
#include <pthread.h>
#include "mouse.h"

int mouse_left, mouse_middle, mouse_right;
int mouse_x = 1024 / 2, mouse_y = 768 / 2;

void left_click(){
    if (mouse_x > 20 && mouse_y > 20)
        draw_sphere(mouse_x, mouse_y, 20, 0, 255, 0);
}

void mouse_poll(){
    int pid;
    pid=fork();
    if (pid!=0){
        printf("mouse pid = %d\n", pid);
        return;
    }
    // Close poll when parent die
    prctl(PR_SET_PDEATHSIG, SIGHUP);
    int fd, bytes;
    unsigned char data[4];
    const char *pDevice = "/dev/input/mice";
    // Open Mouse
    fd = open(pDevice, O_RDWR);
    if(fd == -1){
        printf("ERROR Opening %s\n", pDevice);
        return -1;
    }
    
    signed char dx, dy;
    // Read Mouse
    while(1){
        bytes = read(fd, data, sizeof(data));
        if(bytes > 0) {
            int old_mouse_left = mouse_left;
            mouse_left = data[0] & 0x1;
            mouse_right = data[0] & 0x2;
            mouse_middle = data[0] & 0x4;
            dx = data[1];
            dy = data[2];
            mouse_x += dx;
            mouse_y -= dy;
            if (mouse_left && !old_mouse_left) {
                left_click();
            }
        }
    }
}