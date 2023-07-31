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
func (p Punto) distanciaAlOrigen() float64 {
	return math.Sqrt(float64(p.X*p.X + p.Y*p.Y))
}

// Describe un nuevo punto que resulta de sumar las coordenadas del punto que recibe el mensaje y el dado.
func (p *Punto) Suma(otro Punto) Punto {
	return Punto{X: p.X + otro.X, Y: p.Y + otro.Y}
}

// Setters
func (p *Punto) SetX(x int) {
	p.X = x
}

func (p *Punto) SetY(y int) {
	p.Y = y
}

// Anidar struct's 🐸
type Direccion struct {
	calle  string
	numero int
}

func (dir Direccion) String() string {
	return fmt.Sprintf("Calle %s al %d", dir.calle, dir.numero)
}

type Persona struct {
	nombre       string
	direccion    Direccion
	madre, padre *Persona
}

func (p *Persona) Direccion() string {
	return fmt.Sprintf("%s vive en %s", p.nombre, p.direccion.String())
}

func main() {
	// var p Punto = Punto{X: 1, Y: 3}
	// p = Punto{Y:1} ➡ X:0 por default
	// p = Punto{1, 3} ➡ X:1, Y:3

	// fmt.Println(p)
	// fmt.Printf("%+v\n", p)

	// Acceso a los campos
	// p.X = 4
	// p.Y = 0

	// Punto vacío
	// p = Punto{}

	// var q1 *Punto = &Punto{X: 2, Y: 4}
	// var q2 Punto = *q1
	// fmt.Printf("%p\n", q1)
	// fmt.Printf("%+v\n", q1)
	// fmt.Printf("%+v", q2)

	// q1 = &Punto{Y: 2}
	// q1 = &Punto{1, 6}

	// q1.X = 5 // Mismo acceso

	// q1 = &Punto{}

	// &Punto{} === new(Punto) Son equivalentes. Crea un struc vacío y un puntero al mismo.

	// p1 := &Punto{X: 0}
	// modificarPunto(p1)
	// fmt.Printf("%v", p1)

	p := Punto{1, 1}
	q := &Punto{2, 3}

	fmt.Printf("%f\n", p.distanciaAlOrigen())
	fmt.Printf("%f\n", q.distanciaAlOrigen())

	t := p.Suma(Punto{4, 5})

	fmt.Printf("%v\n", p.Suma(Punto{2, 3}))
	fmt.Printf("%v\n", q.Suma(Punto{2, 3}))
	fmt.Printf("%v\n", t)

	p.SetX(-1)
	fmt.Printf("%v\n", p)

	// -------------------------------------
	jon := Persona{nombre: "Jon Voigth"}
	angie := Persona{"Angelina Jolie", Direccion{"Beverly Hills", 123}, nil, &jon}

	fmt.Printf(angie.padre.nombre)
	// fmt.Printf(angie.direccion.String())

}

// func modificarPunto(p *Punto) {
// 	p.X = -1
// 	p.Y = -1
// }
