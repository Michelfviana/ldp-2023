#include <stdio.h>

int main()
{
    int a, b, c, menor;

    printf("primeiro valor: ");
    scanf("%d", &a);
    printf("segundo valor: ");
    scanf("%d", &b);
    printf("terceiro valor: ");
    scanf("%d", &c);

    if (a < b && a < c)
    {
        menor = a;
    }
    else if (b < c)
    {
        menor = b;
    }
    else
    {
        menor = c;
    }

    printf("MENOR = %d\n", menor);

    return 0;
}