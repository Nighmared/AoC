package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	sol   = "\033[31;47m"
	reset = "\033[0;0m"
)

type direction int8

const (
	forward direction = iota
	down
	up
)

type step struct {
	d direction
	n int
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func parseInput(lines []string) []step {
	res := make([]step, len(lines))
	for i, line := range lines {
		parts := strings.Split(line, " ")
		dirStr := parts[0]
		nStr := parts[1]
		var dir direction
		switch dirStr {
		case "forward":
			dir = forward
		case "down":
			dir = down
		case "up":
			dir = up
		}
		n, err := strconv.Atoi(nStr)
		check(err)
		res[i] = step{d: dir, n: n}
	}

	return res
}

func main() {
	cont, err := os.ReadFile("input.txt")
	check(err)
	contLines := strings.Split(string(cont), "\n")
	steps := parseInput(contLines[:len(contLines)-1])

	xres := 0
	yres := 0

	for _, s := range steps {
		switch s.d {
		case forward:
			xres += s.n
		case down:
			yres += s.n
		case up:
			yres -= s.n
		}
	}
	fmt.Println("Part 1:")
	fmt.Println("Depth: ", yres, " Horizontal distance: ", xres, sol, "Product: ", xres*yres, reset)

	// Part 2
	fmt.Println("===========================================================================")

	xres = 0
	yres = 0
	aim := 0

	for _, s := range steps {
		switch s.d {
		case forward:
			xres += s.n
			yres += aim * s.n
		case down:
			aim += s.n
		case up:
			aim -= s.n
		}
	}
	fmt.Println("Part 2:")
	fmt.Println("Depth: ", yres, " Horizontal distance: ", xres, sol, "Product: ", xres*yres, reset)

}
