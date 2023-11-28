#include <stdio.h>
// #include <helpers.h>

// Escribir una función que reciba el capital inicial, una tasa de interés y un número de años y devuelva el monto final a cobrar.

int esPar(int numero);

double potencia(double base, int exponente);

double monto(double capitalInicial, double tasaInteres, int anios){
    return capitalInicial * potencia((1 + tasaInteres / 100), anios);
}

int main() {
    // Variables para almacenar la entrada del usuario
    double capitalInicial, tasaInteres;
    int anios;

    // Solicitar al usuario que ingrese el capital inicial, la tasa de interés y el número de años
    printf("Ingrese el capital inicial: ");
    scanf("%lf", &capitalInicial);

    printf("Ingrese la tasa de interés (en porcentaje): ");
    scanf("%lf", &tasaInteres);

    printf("Ingrese el número de años: ");
    scanf("%d", &anios);

    // Calcular el monto final utilizando la función monto
    double montoFinal = monto(capitalInicial, tasaInteres, anios);

    // Mostrar el resultado
    printf("El monto final a cobrar después de %d años es: %.2f\n", anios, montoFinal);
    return 0;
}