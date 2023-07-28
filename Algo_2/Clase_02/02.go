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
	pasaUnDiaConPuntero(&dolar)
	fmt.Printf("Ahora vale %d\n", dolar)

	// ----------------------------------------
	// Arrays 🏋🏼‍♀️

	// Secuencia de elementos.
	// Se crean con tamaño fijo que no se puede modificar.
	// Los elementos se encuentran contiguos en memoria.
	// Las posiciones van de 0 a N-1 (siendo N el tamaño del array).

	var arr []int = []int{1, 2, 3, 4}

	fmt.Printf("%d ", arr[0])
	fmt.Printf("%d ", arr[1])
	fmt.Printf("%d ", arr[2])
	fmt.Printf("%d ", arr[3])

	//var arreglo [4]int = [5]int {1,2,3,4} // Parte del tipo de un array es el tamaño que tiene.

	arreglo := [4]int{1, 2, 3}
	// Se imprime el valor por defecto en el último lugar.
	fmt.Println(arreglo)

	modificar(arreglo) // Pasa el array por copia.
	fmt.Println(arreglo)

	// Ahora si... 🙌🏼
	modificarConPuntero(&arreglo)
	fmt.Println(arreglo)

}

func pasaUnDia(valor int) {
	valor = 2 * valor
}

func pasaUnDiaConPuntero(valor *int) {
	*valor = 2 * *valor
}

func modificar(arr [4]int) {
	arr[0] = 0
}

func modificarConPuntero(arr *[4]int) {
	arr[0] = 0
}
