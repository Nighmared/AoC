dir = {
"N":0,
"E":90,
"S":180,
"W":270,
}

steps = {
0: (0,1),
90: (1,0),
180: (0,-1),
270: (-1,0)
}

facing = 90

#a = ["F10","N3","F7","R90","F11"]

with open("input.txt","r") as f:
	lines = f.readlines()


pos_x = 0
pos_y = 0


for i in lines:
	letter = i[:1]
	num = int(i[1:])
	if letter in ("R","L"):
		sign = (1,-1)[letter == "L"]
		facing = (sign*num+facing)%360
	elif letter in ("N","E","S","W"):
		angle = dir[letter]
		d_x,d_y = steps[angle]
		pos_x += num*d_x
		pos_y += num*d_y
	elif letter in ("F","B"):
		sign = (1,-1)[letter =="B"]
		d_x,d_y = steps[facing]
		pos_x += num*sign*d_x
		pos_y += num*sign*d_y
	else:
		print("AAA")


print(abs(pos_x)+abs(pos_y))
