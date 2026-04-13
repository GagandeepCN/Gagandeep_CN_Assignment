#include <stdio.h>

int main() {
    int port = 80;          // variable
    int *ptr = &port;       // pointer

    printf("Port using variable: %d\n", port);
    printf("Port using pointer: %d\n", *ptr);

    // change value using pointer
    *ptr = 443;

    printf("New port value: %d\n", port);

    return 0;
}
