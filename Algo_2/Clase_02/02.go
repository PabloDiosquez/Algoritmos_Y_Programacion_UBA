package main

import "fmt"

func main() {
	// // ¿Cómo usar a los punteros? ☝🏼
	// var dir *int // Declara una variable dir que es un puntero a un int (el tipo de dir es "puntero a int").

	// var numero int
	// dir = &numero // &: Operador de dirección, devuelve la dirección de memoria en la que vive numero (la variable).

	// // Indirección
	// var pepe int = *dir // *: Operador de indirección, devuelve la variable que está en la memoria referenciada por dir.

	var dolar int = 10
	fmt.Printf("Ahora vale %d\n", dolar)
	pasaUnDia(dolar)
	fmt.Printf("Ahora vale %d\n", dolar)

	fmt.Printf("Ahora vale %d\n", dolar)
	pasaUnDiaI(&dolar)
	fmt.Printf("Ahora vale %d\n", dolar)

}

func pasaUnDia(valor int) {
	valor = 2 * valor
}

func pasaUnDiaI(valor *int) {
	*valor = 2 * *valor
}
