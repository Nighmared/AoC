def checkPass(passport:str)->bool:
	req_fields = (
		"byr",
		"iyr",
		"eyr",
		"hgt",
		"hcl",
		"ecl",
		"pid",
	)
	found_fields = 0
	parts = passport.split(" ")
	for field in req_fields:
		field_found = False
		for part in parts:
			if part.startswith(field):
				field_found = True
				break
		if not field_found:
			return False
	return True

def check_part_2(passp:str):
	fields = {}
	for fieldpair in passp.split(" "):
		if(fieldpair.strip() == ""):
			continue
		field,value = fieldpair.split(":")
		fields[field.strip()] = value.strip()
	try:
		return (
			check_byr(fields["byr"]) and 
			check_iyr(fields["iyr"]) and
			check_eyr(fields["eyr"]) and
			check_hgt(fields["hgt"]) and
			check_hcl(fields["hcl"]) and
			check_ecl(fields["ecl"]) and
			check_pid(fields["pid"])
	)
	except KeyError:
		#print("keyerrrorr")
		return False

def check_byr(byr:str):
	out = len(byr) == 4 and byr.isnumeric() and int(byr) >= 1920 and int(byr) <= 2002
	#print("byr is ",out)
	return out
def check_iyr(iyr:str):
	out = len(iyr) == 4 and iyr.isnumeric() and int(iyr) >= 2010 and int(iyr) <= 2020
	#print("iyr is ", out)
	return out

def check_eyr(eyr:str):
	out =  len(eyr) == 4 and eyr.isnumeric() and int(eyr) >= 2020 and int(eyr) <= 2030
	#print("eyr is ", out)
	return out

def check_hgt(hgt:str):
	out = True
	unit_part = hgt[-2:]
	if unit_part == "cm":
		int_part = hgt[:3]
		out =  int_part.isnumeric() and int(int_part)>=150 and int(int_part)<=193
	elif unit_part == "in":
		int_part = hgt[:2]
		out = int_part.isnumeric() and int(int_part)>=59 and int(int_part)<= 76
	else:
		out = False
	#print("hgt is ",out)
	return out

def check_hcl(hcl:str):
	is_valid = True
	is_valid = hcl.startswith("#") and len(hcl) == 7
	if(is_valid):
		for i in range(1,7):
			if hcl[i] not in ("abcdef0123456789"):
				is_valid = False
				break
	#print("hcl is ",is_valid)
	return is_valid

def check_ecl(ecl:str)->bool:
	out =  ecl in ("amb","blu","brn","gry","grn","hzl","oth")
	#print("ecl is ",out)
	return out

def check_pid(pid:str)->bool:
	out =  len(pid) == 9 and pid.isnumeric()
	#print("pid is ", out)
	return out




lines = open("advOfCode4.txt").readlines()
i = 0
currPass = ""
validPasses = 0
passes = []
while i<len(lines):
	currPass = ""
	while(i<len(lines) and lines[i].strip() != ""):
		currPass += " " + lines[i].strip()
		i+=1
	passes.append(currPass)
	if(checkPass(currPass)):
		validPasses += 1
	i+=1

print("Solution part 1: ",validPasses)

validPasses = 0
for passp in passes:
	validPasses+= check_part_2(passp)

print("Solution part 2: ",validPasses)