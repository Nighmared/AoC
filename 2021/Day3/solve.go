package main

import (
	"fmt"
	"os"
	"strings"
)

const (
	sol   = "\033[31;47m"
	reset = "\033[0;0m"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	fmt.Println("Part 1:")
	cont, err := os.ReadFile("input.txt")
	check(err)
	contLines := strings.Split(string(cont), "\n")

	fmt.Println("vars", sol, "result", reset)

	fmt.Println("===========================================================================")
	// PART 2
	fmt.Println("Part 2:")

	fmt.Println("vars", sol, "result", reset)

}
