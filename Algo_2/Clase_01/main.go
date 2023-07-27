package main

import "fmt"

func main() {
	fmt.Println("Hola Mundo!!")

	// Conversiones de Tipos - Ejemplos 🥐
	// var a int = 5
	// var b uint = a  - cannot use a (variable of type int) as uint value in variable declaration

	// Se deben hacer conversiones explícitas
	var a uint16 = 500
	var b uint8 = uint8(a)

	var c uint8 = 250
	var d int8 = int8(c)

	var e float64 = 124.64
	var f int = int(e)

	fmt.Println(a, b) // 500 244
	fmt.Println(c, d) // 250 -6
	fmt.Println(e, f) // 124.64 124

	// ---------------------------------------
	// Variables 💪🏼
	// var x int
	// x = 5

	// var y int = 10

	// z := 3

	// var x1, y1 int
	// x1, y1 = 1, 2

	// var a1, b1 int = 2, 3

	// z1, z2 := -1, -12

	// Constantes 🥶
	const constante1 int = 4

	// ProTip 🙊

	// var ( // o con const
	// 	a int     = 4
	// 	b byte    = 1
	// 	c float32 = 12.2
	// )

	// ---------------------------
	// Funciones
	fmt.Println(sumar(3, 6))        // 9
	fmt.Println(sumarYRestar(2, 7)) // 9 -5

	// ----------------------------
	// Estructuras de control 🕹

	// IF 🐸
	// if condición {
	// 		Bloque de código
	// }

	// if condición {
	// 	Bloque de código 1
	// }else {
	// 	Bloque de código 2
	// }

	// if condición1 {
	// 	Bloque de código 1
	// }else if condición2 {
	// 	Bloque de código 2
	// }else {
	// 	Bloque de código 3
	// }

	// FOR 🥶
	// for ini; condición; incremento{
	// 	Bloque de código
	// }

	// Imprime los números del 0 al 10 de uno en uno.
	for i := 0; i <= 10; i++ {
		fmt.Printf("%d", i) // Imprime con formato
	}

	// WHILE ⚠
	// for condición {
	// 		Bloque de código
	// }
}

// Funciones - I
func sumar(a int, b int) int {
	return a + b
}

// Funciones - II
// func sumarYRestar(a, b int) (int, int){
// 	return a+b, a-b
// }

// Funciones - III
func sumarYRestar(a, b int) (suma int, resta int) {
	suma = a + b
	resta = a - b
	return
}
