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

type block struct {
	Index, Id, Len int
}

type freeListNode struct {
	indx, len int
	active    bool
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func parseInput(inp []byte) ([]block, []int) {
	blocks := make([]block, len(inp)/2)
	disk := make([]int, 0)
	stripped := strings.Trim(string(inp), "\n")

	block_id := 0
	free_block := false
	for _, s := range stripped {
		blen := int(s - '0')
		to_add := block_id
		if free_block {
			to_add = -1
		} else {
			blocks = append(blocks, block{Index: len(disk), Id: block_id, Len: blen})
			block_id++
		}
		for i := 0; i < blen; i++ {
			disk = append(disk, to_add)
		}
		free_block = !free_block
	}

	return blocks, disk
}

func part1(disk []int) uint64 {
	disklen := len(disk)
	first_free := 0
	for i := disklen - 1; i >= 0; i-- {
		blck := disk[i]

		if blck < 0 {
			continue
		}
		broke := false
		for disk[first_free] > -1 {
			first_free++
			if first_free >= disklen {
				broke = true
				break
			}
		}
		if broke {
			break
		}
		if i <= first_free {
			break
		}
		disk[first_free] = blck
		disk[i] = -1
		continue

	}
	res := uint64(0)
	for i, b := range disk {
		if b < 0 {
			break
		}
		// fmt.Println("{}{}", i, b)
		res += uint64(i * b)
	}

	return res
}

func part2(disk []int, blocks []block) int {
	blockslen := len(blocks)
	free_list := make([]freeListNode, 0)
	free_start := 0
	free_len := 0
	for i, b := range disk {
		if b < 0 {
			if free_len == 0 {
				free_start = i
			}
			free_len++
		} else {
			if free_len > 0 {
				free_list = append(free_list, freeListNode{indx: free_start, len: free_len, active: true})
				free_len = 0
			}
		}
	}
	finish := false
	for j := blockslen - 1; j >= 0; j-- {
		curr_block := blocks[j]
		for k := 0; k < len(free_list); k++ {
			free_node := &free_list[k]
			if !free_node.active {
				continue
			}
			if curr_block.Index <= free_node.indx {
				break
			}
			if free_node.len >= curr_block.Len {
				for i := 0; i < curr_block.Len; i++ {
					disk[curr_block.Index+i] = -1
					disk[free_node.indx+i] = curr_block.Id
				}
				if free_node.len > curr_block.Len {
					free_node.len -= curr_block.Len
					free_node.indx += curr_block.Len
				} else {
					free_node.active = false
				}
				break
			}
		}
		if finish {
			break
		}
	}

	res := 0
	for i, b := range disk {
		if b < 0 {
			continue
		}
		res += i * b
	}
	return res
}

func main() {
	cont, err := os.ReadFile("input.txt")
	check(err)
	_, disk := parseInput(cont)
	disk1 := make([]int, len(disk))

	fmt.Println("Part 1:")
	copy(disk1, disk)
	fmt.Println(part1(disk1))

	// Part 2
	// fmt.Println("===========================================================================")
	// copy(disk1, disk)
	// fmt.Println("Part 2:")
	// fmt.Println(part2(disk1, blocks))

}
