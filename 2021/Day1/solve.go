package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func convToInts(lines []string) []int64 {
	res := make([]int64, len(lines))
	for i, line := range lines {
		lineInt, err := strconv.ParseInt(line, 10, 64)
		check(err)
		res[i] = lineInt
	}
	return res
}

func main() {
	cont, err := os.ReadFile("input.txt")
	check(err)
	splitCont := strings.Split(string(cont), "\n")
	depths := convToInts(splitCont[:len(splitCont)-1]) // last one is just empty string
	oldVal := depths[0]
	counter := 0
	for _, depth := range depths {
		if depth > oldVal {
			counter++
		}
		oldVal = depth
	}
	fmt.Println("Number of increasing dephts found: ", counter)

	// PART2
	currPos := 3
	currSum := depths[0] + depths[1] + depths[2]
	oldSum := currSum
	counter = 0
	for currPos < len(depths) {
		oldSum = currSum
		currSum -= depths[currPos-3]
		currSum += depths[currPos]
		if oldSum < currSum {
			counter++
		}
		currPos++
	}

	fmt.Println("Number of sliding window increases: ", counter)

}
