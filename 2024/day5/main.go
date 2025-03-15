package main

import (
	"bufio"
	"log"
	"os"
)

// read file input.txt and store in string
func readInput(filename string) string {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	r := bufio.NewReader(f)
	temp, err := r.ReadString('|')
	if err != nil {
		log.Fatal(err)
	}
	return temp
}

func main() {
	FILE := "example.txt"
	input := readInput(FILE)
	println(input)
}
