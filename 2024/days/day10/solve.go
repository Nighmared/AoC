package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func parseInput(inp []byte) ([][]int, [][]int, map[[]int]bool)

func main() {
	cont, err := os.ReadFile("input.txt")
	check(err)
	blocks, disk := parseInput(cont)
	disk1 := make([]int, len(disk))

	fmt.Println("Part 1:")
	copy(disk1, disk)
	fmt.Println(part1(disk1))

	fmt.Println("Part 2:")
	fmt.Println(part2(disk, blocks))

}
