package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Strings ☂
	var c rune
	for _, c = range "おはよう Algo 2" {
		fmt.Printf("Símbolo %c - Código Unicode %d\n", c, c)
	}

	// Leer input de usuario 🐣
	fmt.Println("Ingrese un input:")
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	fmt.Printf("Leí: %s", s.Text())

	// Leer un archivo 🗄
	// const ruta = "archivo.txt"

	// archivo, err = os.Open(ruta)
	// if err != nil {
	// 	fmt.Printf("Archivo %s no encontrado", ruta)
	// 	return
	// }
	// defer archivo.Close()

	// s := bufio.NewScanner(archivo)
	// for s.Scan() {
	// 	fmt.Printf("Leí: %s\n", s.Text())
	// }
	// err := s.Err()
	// if err != nil {
	// 	fmt.Printf(err)
	// }
}
