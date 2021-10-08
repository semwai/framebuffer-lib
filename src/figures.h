#ifndef FIGURES
#define FIGURES
/*
Прямоугольник
*/
void draw_rect(int x1, int y1, int x2, int y2, int r, int g, int b);
/*
Заполненная сфера
*/
void draw_sphere(int x1, int y1, int rad, int r, int g, int b);
/*
Круг со стенкой размером radout - radin
*/
void draw_circle(int x1, int y1, int radin, int radout, int r, int g, int b);
/*
Черный экран
*/
void clear_screen();

#endif