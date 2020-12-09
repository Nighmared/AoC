preAmLen = 25

lines = open("input.txt").readlines()
vals = []
for i in range(0,preAmLen):
	vals.append(int(lines[i]))
wrongNum = -1
for i in range(preAmLen,len(lines)):
	vals.append(int(lines[i]))
	currNum = int(lines[i])
	summAble = False
	for a in range(i-preAmLen,i):
		aVal = int(lines[a])
		for b in range(i-preAmLen,i):
			bVal = int(lines[b])
			if a == b:
				continue
			if(aVal+bVal == currNum):
				summAble = True
				break
		if(summAble):
			break
	if not summAble:
		wrongNum = currNum
		print(currNum)
		break

for i in range(1,len(lines)):
	currS = 0
	lowIndex = 0
	high_index = i-1
	for a in range(0,i):
		currS += int(lines[a])
	while(high_index<len(lines)-1):
		if(currS == wrongNum):
			amin = max(vals)
			amax = -1
			for i in range(lowIndex,high_index+1):
				amin = min(int(lines[i]),amin)
				amax = max(int(lines[i]),amax)
			print(amin+amax," RES")
			break
		currS -= int(lines[lowIndex])
		lowIndex+=1


		high_index+=1
		currS += int(lines[high_index])

