package main

import "fmt"

type Punto struct { // Tipo nuevo
	// Campos o miembros
	X int
	Y int
}

func main() {
	var p Punto = Punto{X: 1, Y: 3}
	// p = Punto{Y:1} ➡ X:0 por default
	// p = Punto{1, 3} ➡ X:1, Y:3

	fmt.Println(p)
	fmt.Printf("%+v\n", p)

	// Acceso a los campos
	p.X = 4
	p.Y = 0

	// Punto vacío
	// p = Punto{}

	var q *Punto = &Punto{X: 2, Y: 4}

	fmt.Printf("%p\n", q)
	fmt.Printf("%+v", q)

	q = &Punto{Y: 2}
	q = &Punto{1, 6}

	q.X = 5 // Mismo acceso

	q = &Punto{}

	// &Punto{} === new(Punto) Crea un struc vacío y un puntero al mismo.
}
