from collections import defaultdict
with open("input.txt","r") as f:
	lines = f.readlines()



left = []
right = []
cnt:dict[int,int] = defaultdict(int)


for line in lines:
	a,b = line.strip().split("  ")
	c,d = int(a),int(b)
	left.append(c)
	right.append(d)
	cnt[d]+=1

assert len(left) == len(right)
left_s = sorted(left)
right_s = sorted(right)

res = 0
for i in range(len(left)):
	res += abs(left_s[i]-right_s[i])
print("[Part 1]",res)


#####

res2 = 0
for x in left:
	res2+= x*cnt[x]

print("[Part 2]", res2)
