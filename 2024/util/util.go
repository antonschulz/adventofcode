package util

import (
	"log"
	"os"
)

// read file input.txt and store in string
func readInput(filename string) string {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}
