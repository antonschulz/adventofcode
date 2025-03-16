package main

import (
	"errors"
	"fmt"
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

func convertInputToGrid(input string, reverse bool) [][]string {
	width := 0
	for _, c := range input {
		if c == '\n' {
			break
		}
		width++
	}
	height := len(input) / width
	grid := make([][]string, height)
	for i := range grid {
		grid[i] = make([]string, width)
	}
	fmt.Println(grid[9][9])
	fmt.Println("width: ", width, "height: ", height, "maxlen: ", len(input))

	if !reverse {
		y := height - 1
		x := 0
		for _, c := range input {
			if c == '\n' {
				y--
				x = 0
				continue
			} else {
				grid[y][x] = string(c)
				x++
			}
		}
	} else {
		y := 0
		x := 0
		for _, c := range input {
			if c == '\n' {
				y++
				x = 0
				continue
			} else {
				grid[y][x] = string(c)
				x++
			}
		}
	}
	fmt.Println(grid[3])
	return grid
}

// returns y, x coordinates for guard and direction
func findGuard(grid [][]string) ([]int, string, error) {
	for y, row := range grid {
		for x, c := range row {
			if c == "^" || c == "<" || c == ">" || c == "v" {
				return []int{y, x}, c, nil
			}
		}
	}
	return []int{0, 0}, "", errors.New("could not find string")

}

func p1(grid [][]string) {
	ymax, xmax := len(grid)-1, len(grid[0])-1
	coords, guard, err := findGuard(grid)
	if err != nil {
		panic(err)
	}
	x, y := coords[1], coords[0]
	visited := 1 // One of-error for input if set to 1???
	grid[y][x] = "X"
	for {
		switch guard {
		case "^":
			if y < ymax && grid[y+1][x] != "#" {
				y++
				if grid[y][x] != "X" {
					visited++
				}
				if grid[y-1][x] != "X" {
					panic("^")
				}
				grid[y][x] = "X"
			} else if y < ymax && grid[y+1][x] == "#" {
				guard = ">"
				continue
			} else {
				fmt.Println("Part 1: ", visited)
				//printGrid(grid)
				fmt.Println(grid[y][x])

				return
			}
		case "v":
			if y > 0 && grid[y-1][x] != "#" {
				y--
				if grid[y][x] != "X" {
					visited++
				}
				if grid[y+1][x] != "X" {
					panic("v")
				}
				grid[y][x] = "X"
			} else if y > 0 && grid[y-1][x] == "#" {
				guard = "<"
				continue
			} else {
				fmt.Println("Part 1: ", visited)

				return
			}
		case ">":
			if x < xmax && grid[y][x+1] != "#" {
				x++
				if grid[y][x] != "X" {
					visited++
				}
				if grid[y][x-1] != "X" {
					panic(">")
				}
				grid[y][x] = "X"
			} else if x < xmax && grid[y][x+1] == "#" {
				guard = "v"
				continue
			} else {
				fmt.Println("Part 1: ", visited)

				return
			}
		case "<":
			if x > 0 && grid[y][x-1] != "#" {
				x--
				if grid[y][x] != "X" {
					visited++
				}
				if grid[y][x+1] != "X" {
					panic("<")
				}
				grid[y][x] = "X"
			} else if x > 0 && grid[y][x-1] == "#" {
				guard = "^"
				continue
			} else {
				fmt.Println("Part 1: ", visited)

				return
			}
		default:
			panic("sdf")
		}

	}
}

func printGrid(grid [][]string) {
	height := len(grid)
	width := len(grid[0])

	for i := height - 1; i >= 0; i-- {
		fmt.Println()
		for j := range width {
			fmt.Print(grid[i][j])
		}
	}
}

func main() {
	FILE := "input.txt"
	input := readInput(FILE)
	grid := convertInputToGrid(input, false)
	p1(grid)
}
