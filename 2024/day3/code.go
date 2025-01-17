package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

// read file input.txt and store in string
func readInput(filename string) string {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}

func part1(input string) int {
	mulreg := `mul\(([1-9]+\d?\d?),([1-9]+\d?\d?)\)`
	re, err := regexp.Compile(mulreg)
	if err != nil {
		fmt.Println("Could not compile regex")
		panic(err)
	}

	// -1 for all matches
	matches := re.FindAllStringSubmatch(input, -1)

	sum := 0
	for _, match := range matches {
		i, err := strconv.Atoi(match[1])
		if err != nil {
			panic(err)
		}
		j, err := strconv.Atoi(match[2])
		if err != nil {
			panic(err)
		}
		res := i * j
		sum += res
	}
	fmt.Println("Part 1: ", sum)
	return 0
}

func part2(input string) int {
	dontreg := `mul\(([1-9]+\d?\d?),([1-9]+\d?\d?)\)|(do\(\))|(don't\(\))`
	re, err := regexp.Compile(dontreg)
	if err != nil {
		fmt.Println("Could not compile regex")
		panic(err)
	}
	// replace all matches with empty string
	matches := re.FindAllStringSubmatch(input, -1)
	enabled := true
	sum := 0
	for _, match := range matches {
		switch match[0] {
		case "do()":
			enabled = true
			continue
		case "don't()":
			enabled = false
			continue
		default:
			if enabled {
				i, err := strconv.Atoi(match[1])
				if err != nil {
					panic(err)
				}
				j, err := strconv.Atoi(match[2])
				if err != nil {
					panic(err)
				}
				res := i * j
				sum += res
			}
		}
	}
	fmt.Println("Part 2: ", sum)
	return 0

}

func main() {
	s := readInput("input.txt")
	part1(s)
	part2(s)
}
