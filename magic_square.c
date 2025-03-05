#include <stdio.h>
#include <stdlib.h>

int draw_square(int n, int square[]) {
    int m = 0;
    for (int j = 0; j < n; j++) {
        printf("----");
    }
    printf("\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("| %d ", square[m]);
            m++;
        }
        printf("|\n");
        for (int j = 0; j < n; j++) {
            printf("----");
        }
        printf("\n");
    }
    return 1;
}

int determine_square(int n) {
    if (n % 2 == 0) {
        return 0;
    }

    int x = (n / 2);
    int y = n - 1;
    int square[n * n];

    for (int index = 0; index < n*n; index++) {
        square[index] = 0;
    }

    int i = 1;
    while(1) {
        if (square[y * n + x] == 0) {
            square[y * n + x] = i;
            y++;
            x++;
            i++;
        } else {
            y++;
            x--;
        }
        if (i == n * n + 1) {
            draw_square(n, square);
            return 1;
        }
        if (y < 0) { y += n;} else if (y >  n - 1) { y -= n; }
        if (x < 0) { x += n;} else if (x > n - 1) { x -= n; }
    }
}

int main() {
    int n;
    printf("Gebe eine ungerade Zahl ein, deren magisches Viereck du erzeugen willst:\n");
    scanf("%d", &n);
    determine_square(n);
    return 1;
}
