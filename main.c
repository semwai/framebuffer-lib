#include <unistd.h>
#include "src/figures.h"
#include "src/mouse.h"
#include "src/init.h"
#include "src/demos.h"

int main()
{
    int res = init_buffer();
    if (res)
        return res;
    mouse_poll();
    demo1();
    demo2();
    sleep(15);
    close_buffer();
    return 0;
}