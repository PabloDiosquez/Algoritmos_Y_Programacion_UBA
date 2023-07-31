package main

import (
	"fmt"
	"math"
)

type Punto struct { // Tipo nuevo
	// Campos o miembros
	X int
	Y int
}

// Métodos (Comportamiento 🚀)

// Describe la distancia del punto dado al origen de coordenadas.
func distanciaAlOrigen(p Punto) float64 {
	return math.Sqrt(float64(p.X*p.X + p.Y*p.Y))
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

	var q1 *Punto = &Punto{X: 2, Y: 4}
	var q2 Punto = *q1
	fmt.Printf("%p\n", q1)
	fmt.Printf("%+v\n", q1)
	fmt.Printf("%+v", q2)

	q1 = &Punto{Y: 2}
	q1 = &Punto{1, 6}

	q1.X = 5 // Mismo acceso

	q1 = &Punto{}

	// &Punto{} === new(Punto) Son equivalentes. Crea un struc vacío y un puntero al mismo.

	p1 := &Punto{X: 0}
	modificarPunto(p1)
	fmt.Printf("%v", p1)

}

func modificarPunto(p *Punto) {
	p.X = -1
	p.Y = -1
}
