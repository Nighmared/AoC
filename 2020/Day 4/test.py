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
	for field,validity in req_fields:
		field_found = False
		for part in parts:
			if part.startswith(field):
				field_found = True
				break
		if not field_found:
			return False
	return True

def check_part_2(passy:str):
	print("asdf")
	fields = {}
	for fieldpair in pass.split(" "):
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
		return False

def check_byr(byr:str):
	return len(byr) == 4 and byr.isnumeric() and int(byr) >= 1920 and int(byr) <= 2002

def check_iyr(iyr:str):
	return len(iyr) == 4 and iyr.isnumeric() and int(iyr) >= 2010 and int(iyr) <= 2020

def check_eyr(eyr:str):
	return len(eyr) == 4 and eyr.isnumeric() and int(eyr) >= 2020 and int(eyr) <= 2030

def check_hgt(hgt:str):
	int_part = hgt[:3]
	unit_part = hgt[3:]
	if unit_part == "cm":
		return int_part.isnumeric() and int(int_part)>=150 and int(int_part)<=193
	elif unit_part == "in":
		return int_part.isnumeric() and int(int_part)>=59 and int(int_part)<= 76
	else:
		return False

def check_hcl(hcl:str):
	is_valid = True
	is_valid = hcl.startswith("#") and len(hcl) == 7
	if not is_valid:
		return False
	for i in range(1,8):
		if hcl[i] not in ("abcdef"):
			return False
	return True

def check_ecl(ecl:str)->bool:
	return ecl in ("amb","blu","brn","gry","grn","hzl","oth")

def check_pid(pid:str)->bool:
	return len(pid) == 9 and pid.isnumeric()




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
	passes.append[currPass]
	if(checkPass(currPass)):
		validPasses += 1
	i+=1

print("Solution part 1: ",validPasses)

validPasses = 0
for pass in passes:
	validPasses += int(check_part_2(pass))