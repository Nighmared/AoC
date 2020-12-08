class Computer:
	def __init__(self):
		self.accumulator = 0
		self.executed_lines = []
		self.program = []
		self.instr_pointer = 0
		self.possible_exchange_lines = []
		self.instr_count = 0
	
	def readfile(self,filename:str):
		lines = open(filename).readlines()
		for line in lines:
			instr_op = line[:3]
			instr_arg = int(line[5:].rstrip("\n"))*(1,-1)[line[4:5] == "-"]
			instr_tuple = (instr_op, instr_arg)
			self.program.append(instr_tuple)
			if(instr_op in ("jmp","nop")):
				self.possible_exchange_lines.append((self.instr_count,instr_op,instr_arg)) #line number, op, arg
			self.instr_count+=1

	def reset(self):
		self.instr_pointer = 0
		self.executed_lines.clear()
		self.accumulator = 0

	def work(self):
		while self.instr_pointer not in self.executed_lines and self.instr_pointer<self.instr_count:
			current_instr = self.program[self.instr_pointer]
			self.executed_lines.append(self.instr_pointer)
			if(current_instr[0] == "acc"):
				self.accumulator += current_instr[1]
				self.instr_pointer+=1
			elif(current_instr[0] == "nop"):
				self.instr_pointer+=1
			elif(current_instr[0] == "jmp"):
				self.instr_pointer += current_instr[1]
		if(self.instr_pointer== self.instr_count):
			#print("Accumulator after Program successfully terminates = ",self.accumulator)
			return True
		else:
			#print("Accumulator just before infin loop = ",self.accumulator)
			return False
			
		
	def try_fix(self):
		for candidate in self.possible_exchange_lines:
			line_number = candidate[0]
			line_op = candidate[1]
			line_arg = candidate[2]
			new_line_op = ("nop","jmp")[line_op=="nop"]
			self.program[line_number] = (new_line_op,line_arg)
			if(self.work()):
				print(f"== Res for part2: {self.accumulator} ==")
				return
			else:
				self.program[line_number] = (line_op,line_arg)
				self.reset()

		



solver = Computer()
solver.readfile("advOfCode8.txt")
solver.work()
print(f"== Res for part1: {solver.accumulator} ==")
solver.reset()
solver.try_fix()