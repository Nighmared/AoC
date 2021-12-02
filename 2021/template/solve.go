package main

import (
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	cont, err := os.ReadFile("input.txt")
	check(err)
	contLines := strings.Split(string(cont), "\n")

}
