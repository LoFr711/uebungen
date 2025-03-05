#include <stdio.h>
#include <stdlib.h>

int add(int a, int b) {
    if (b > 0) {
        a++;
        b--;
        return add(a, b);
    } else {
        return a;
    }
}

int mult(int a, int b) {
    if (b > 0) {
        b--;
        return add(a, mult(a, b));
    } else {
        return 0;
    }
}

int main() {
    return 1;
}