lines = open("advOfCode1.txt").readlines();
vals = [];
for line in lines:
	vals.append(int(line))

for i in range(0,len(vals)):
	for j in range(i,len(vals)):
		if(vals[i]+vals[j] == 2020):
			print(vals[i]*vals[j])