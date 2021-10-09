#include <stdlib.h>
#include <stdio.h>


void get_buffer2d(int x1, int y1, int x2, int y2, int* out[]) {
    printf("%x ", out);
    int i, j;
    for (i = y1; i < y2; i++)
        for (j = x1; j < x2; j++) {
            out[i][j] = i * j;
        }
     
}