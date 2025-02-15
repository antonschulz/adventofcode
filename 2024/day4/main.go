package main

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

func charAtIndex(index int, input string, char byte) bool {
	if index < len(input) {
		//println(string(input[index]))
		if input[index] == char {
			return true
		}
		return false
	}
	return false
}

func part1(input string) int {
	// "XMAS -> "SAMX"
	rowLength := 1
	for _, c := range input {
		if c == '\n' {
			break
		}
		rowLength++
	}

	numRows := len(input) / rowLength
	_ = numRows
	count := 0
	for i, c := range input {

		if c == 'X' {
			// horizontal
			println("horizontal:")
			if charAtIndex(i+1, input, 'M') && charAtIndex(i+2, input, 'A') && charAtIndex(i+3, input, 'S') {
				count++
			}
			println("vertical:")
			// vertical
			if charAtIndex(i+(rowLength), input, 'M') && charAtIndex(i+(2*rowLength), input, 'A') && charAtIndex(i+(3*rowLength), input, 'S') {
				count++
			}
			// diagonal right
			println("diag right:")
			if charAtIndex(i+(rowLength)+1, input, 'M') && charAtIndex(i+(2*rowLength)+2, input, 'A') && charAtIndex(i+(3*rowLength)+3, input, 'S') {
				count++
			}
			// diagonal left
			println("diag right:")
			if charAtIndex(i+(rowLength)-1, input, 'M') && charAtIndex(i+(2*rowLength)-2, input, 'A') && charAtIndex(i+(3*rowLength)-3, input, 'S') {
				count++
			}
		}
		// reverse
		if c == 'S' {
			// horizontal
			println("horizontal:")
			if charAtIndex(i+1, input, 'A') && charAtIndex(i+2, input, 'M') && charAtIndex(i+3, input, 'X') {
				count++
			}
			println("vertical:")
			// vertical
			if charAtIndex(i+(rowLength), input, 'A') && charAtIndex(i+(2*rowLength), input, 'M') && charAtIndex(i+(3*rowLength), input, 'X') {
				count++
			}
			// diagonal right
			println("diag right:")
			if charAtIndex(i+(rowLength)+1, input, 'A') && charAtIndex(i+(2*rowLength)+2, input, 'M') && charAtIndex(i+(3*rowLength)+3, input, 'X') {
				count++
			}
			// diagonal left
			println("diag left:")
			if charAtIndex(i+(rowLength)-1, input, 'A') && charAtIndex(i+(2*rowLength)-2, input, 'M') && charAtIndex(i+(3*rowLength)-3, input, 'X') {
				count++
			}
		}
	}
	println()
	println("count was: ", count)
	println("rowlength: ", rowLength)
	println("columnsize: ", numRows)
	return 0
}

// checks 3x3 square (start at index) for XMAS
func checkSquareForX(i int, input string, rowLength int) bool {
	// scenario 1
	if charAtIndex(i, input, 'M') && charAtIndex(i+(rowLength)+1, input, 'A') && charAtIndex(i+(2*rowLength)+2, input, 'S') {
		if charAtIndex(i+2, input, 'M') && charAtIndex(i+1+(rowLength), input, 'A') && charAtIndex(i+(2*rowLength), input, 'S') {
			return true
		}
		if charAtIndex(i+2, input, 'S') && charAtIndex(i+1+(rowLength), input, 'A') && charAtIndex(i+(2*rowLength), input, 'M') {
			return true
		}
	}

	if charAtIndex(i, input, 'S') && charAtIndex(i+(rowLength)+1, input, 'A') && charAtIndex(i+(2*rowLength)+2, input, 'M') {
		if charAtIndex(i+2, input, 'M') && charAtIndex(i+1+(rowLength), input, 'A') && charAtIndex(i+(2*rowLength), input, 'S') {
			return true
		}
		if charAtIndex(i+2, input, 'S') && charAtIndex(i+1+(rowLength), input, 'A') && charAtIndex(i+(2*rowLength), input, 'M') {
			return true
		}
	}
	return false
}

func part2(input string) int {
	// "XMAS -> "SAMX"
	rowLength := 1
	for _, c := range input {
		if c == '\n' {
			break
		}
		rowLength++
	}

	count := 0
	for i, _ := range input {
		if checkSquareForX(i, input, rowLength) {
			count++
		}
	}
	println("part2 count: ", count)
	return 0
}

func main() {
	FILE := "input.txt"
	input := readInput(FILE)
	part1(input)
	part2(input)
}
