package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
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
	fmt.Println("Depth: ", yres, " Horizontal distance: ", xres, "Product: ", xres*yres)

	// Part 2

}
