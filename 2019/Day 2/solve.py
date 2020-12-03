from Computer import Computer

print()
solver = Computer("input.txt")
#PART 1: replace pos 1 with 12 and pos 2 with 2
solver.set(1,12)
solver.set(2,2)
solver.work()
print("solution for part1 (value of index 0 after computation): ", solver.get(0) )

#PART 2: find combination of values at index 1 (noun) and 2 (verb) that result in 19690720 and output 100*noun + verb

noun = 0
while(noun <100):
	for verb in range(0,99):
		solver.reset() #clean up
		solver.set(1,noun)
		solver.set(2,verb)
		solver.work()
		if(solver.get(0) == 19690720):
			print("Solution to part2: ", noun*100+verb)
			noun = 100
			break
	noun += 1
			





