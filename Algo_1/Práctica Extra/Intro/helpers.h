
/**
 * Calcula el cuadrado de un número.
 *
 * @param numero Número que se desea elevar al cuadrado.
 * @return El cuadrado del número proporcionado.
 */
double cuad(double numero) {
    return numero * numero;
}

/**
 * Calcula la potencia de una base elevada a un exponente.
 *
 * @param base La base de la potencia.
 * @param exponente El exponente al cual se eleva la base.
 * @return El resultado de elevar la base al exponente.
 *         Si la base es 0 y el exponente es 0 o negativo, devuelve -1 como indicador de error.
 *         Para exponentes negativos, se maneja de manera adecuada para obtener resultados fraccionarios.
 */
double potencia(double base, int exponente) {
    // Caso base: cualquier número elevado a la potencia 0 es 1
    if (exponente == 0) {
        return 1;
    }

    // Manejo de exponentes negativos
    if (exponente < 0) {
        return 1 / potencia(base, -exponente);
    }

    // Manejo de base igual a 0 y exponente 0 o negativo (indefinido)
    if (base == 0 && exponente <= 0) {
        printf("Error: Base igual a 0 con exponente 0 o negativo no definido.\n");
        return -1; // Puedes devolver un valor especial o manejar el error de otra manera
    }

    // Optimización para exponentes pares
    if (esPar(exponente)) {
        double mitadPotencia = potencia(base, exponente / 2);
        return mitadPotencia * mitadPotencia;
    } else {
        double mitadPotencia = potencia(base, exponente / 2);
        return mitadPotencia * mitadPotencia * base;
    }
}

/**
 * Verifica si un número entero es par.
 *
 * @param numero Número entero que se desea verificar.
 * @return 1 (verdadero) si el número es par, 0 (falso) si es impar.
 */
int esPar(int numero) {
    return numero % 2 == 0;
}