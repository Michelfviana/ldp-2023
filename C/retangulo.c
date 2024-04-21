#include <stdio.h> 
#include <math.h>

int main()
{
    double base, altura, area, perimetro, diagonal;

    printf("base do retângulo: ");
    scanf("%lf", &base);

    printf("altura do retângulo: ");
    scanf("%lf", &altura);

    area = base * altura;
    perimetro = 2 * (base + 2 * altura);
    diagonal = sqrt(pow(base, 2.0) + pow(altura, 2.0));

    printf("AREA = %.4lf\n", area);
    printf("PERÍMETRO = %.4lf\n", perimetro);
    printf("DIAGONAL = %.4lf\n", diagonal);
    
    return 0;
}
