#include <stdio.h> 

int main() {

    double nota1, nota2, notaFinal;

    printf("digite a primeira nota: ");
    scanf("%lf", &nota1);

    printf("digite a segunda nota: ");
    scanf("%lf", &nota2);

    notaFinal = nota1 + nota2;
    printf("NOTA FINAL = %.1lf\n", notaFinal);

    if (notaFinal < 60.0) {
        printf("REPROVADO\n");
    }
    
    return 0;
}