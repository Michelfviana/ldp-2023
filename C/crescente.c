#include <stdio.h>

int main()
{
    int x, y;

    printf("Digite dois números:\n");
    scanf("%d,", &x);
    scanf("%d,", &y);

    while (x != y) {
        if (x < y) {
            printf("CRESCENTE\n");
        }
        else {
            printf("Decrescente\n");
        }

        printf("Digite outros dois números:\n");
        scanf("%d,", &x);
        scanf("%d,", &y);
    }
    return 0;
}
