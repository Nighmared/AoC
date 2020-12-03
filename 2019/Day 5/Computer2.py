
class Computer:
	IMM_OP = (3,4)
	ARG_OP = (1,2)
	DEBUG = False
	instr_log = []
	inval = -1
	def __init__(self,fName):
		self.fname = fName
		self.memory = {}
		self._readInput()
		self.printcount = 0

	def reset(self):
		self.printcount = 0
		self.instr_log.clear()
		self.memory = self.__reset_memory.copy()

	def _readInput(self):
		arr_of_strings = open(self.fname).read().split(",")
		for i in range(0,len(arr_of_strings)):
			self.memory[i] = int(arr_of_strings[i])

		self.__reset_memory = self.memory.copy()

	def get(self,index):
		return self.memory[index]
	def set(self,index,value):
		self.memory[index] = value

	def work(self):
		instr_pointer = 0
		instr = self.memory[instr_pointer]
		op_code = instr%100
		print("******************************")
		while(op_code != 99):
			mode_first = int(instr/100)%10 # C
			mode_second = int(instr/1000)%10 # B
			mode_third = int(instr/10000)%10 # A


			if(op_code in self.IMM_OP):
				if(self.DEBUG): print("at pos:",instr_pointer," =>  " ,instr,self.memory[instr_pointer+1])
				self.instr_log.append((instr_pointer,instr,self.memory[instr_pointer+1]))
				a = self.memory[instr_pointer+1]
				self._do_op_imm(op_code,mode_first,a)
				instr_pointer+=2
				#print("did imm op, increased instr pointer to ",instr_pointer)
			elif(op_code in self.ARG_OP):
				if(self.DEBUG): print("at pos:",instr_pointer," =>  " ,instr,self.memory[instr_pointer+1],self.memory[instr_pointer+2],self.memory[instr_pointer+3])
				a = self.memory[instr_pointer+1]
				b = self.memory[instr_pointer+2]
				c = self.memory[instr_pointer+3]
				memvala,memvalb = 0,0
				if(mode_first == 0):
					memvala = self.memory[a]
				if(mode_second == 0):
					memvalb = self.memory[b]
				self.instr_log.append((instr_pointer,instr,self.memory[instr_pointer+1],self.memory[instr_pointer+2],self.memory[instr_pointer+3],memvala,memvalb))

				self._do_op_arg(
					op_code,
					a,mode_first,
					b,mode_second,
					c,mode_third)
				instr_pointer+=4
			else:
				print("===================\n oh no we got an error")
				print("heres some info")
				print(instr_pointer)
				for a in (-3,-2,-1,0,1,2,3):
					print(self.memory[instr_pointer+a],end=" ")
				print("\n")
				print(f"unknown opcode >{op_code}< found! ")
				return #dont raise error cuz output gets uselessly messy

			instr = self.memory[instr_pointer] # fetch next instr
			op_code = instr%100 # get opcode
		print("******************************\n")

	def _do_op_arg(
		self,
		op_code:int,
		first_arg:int, mode_first_arg:int,
		sec_arg:int, mode_sec_arg:int,
		third_arg:int, mode_third_arg:int):
		#FIRST: GET ALL VALUES
		val1 = val2 = res_indx = 0

		if(mode_first_arg == 1):
			val1 = first_arg
		else:
			val1 = self.memory[first_arg]

		if(mode_sec_arg == 1):
			val2 = sec_arg
		else:
			val2 = self.memory[sec_arg]

		#if(mode_third_arg == 1):
		#	res_indx = third_arg
		#else:
		#	res_indx = self.memory[third_arg]
		res_indx = third_arg

		if(op_code == 1):
			self.memory[res_indx] = val1 + val2
			if(self.DEBUG):print(f"stored {val1}+{val2} = {val1+val2} at self.memory[{res_indx}] ")
		elif(op_code == 2):
			self.memory[res_indx] = val1 * val2
			if(self.DEBUG): print(f"stored  {val1}*{val2} = {val1*val2} at self.memory[{res_indx}] ")
		else:
			raise ValueError("wtf this shouldnt be possible lol")
	
	def _do_op_imm(
		self,
		op_code:int,
		mode:int,
		arg:int
		):
		address = 0
		if(mode == 1 or op_code == 3):
			defin_arg = arg
		else:
			defin_arg = self.memory[arg]
		
		if(op_code == 3):
			if(self.inval == -1):
				val = int(input("give input: "))
				self.memory[defin_arg] = val
			else:
				print(f"give input: {self.inval}")
				self.memory[defin_arg] = self.inval
			print()
		elif(op_code == 4):
			self.printcount+= 1
			end = "\n"
			if defin_arg == 0: end = "\r"
			print(f"[IntComp] {str(self.printcount).ljust(3)}>\t{defin_arg}",end = end)
			if defin_arg!=0 and abs(defin_arg)<10000:
				for i in range(10,0,-1):
					print(self.__parse_log_entry(self.instr_log[-i]))

		else:
			raise ValueError("neither should this be possible lol")

	def __parse_log_entry(self,entry:tuple) -> str:
		opcode = entry[1]
		instr_ad = entry[0]
		arg1s = entry[2:]
		out = ""
		out += str(instr_ad)+" =>\t"
		out += str(entry[1:])
		out += "\t"
		out += "#" 
		if opcode%100 == 1:
			out+= "add"
		elif opcode%100 == 2:
			out+= "multiply"
		elif opcode%100 == 3:
			out+= "input"
		elif opcode%100 == 4:
			out+= "==================output"
		elif opcode%100 == 5:
			out += "TODO NEWOP"
		elif opcode%100 == 6:
			out += "TODO NEWOP"
		elif opcode%100 == 7:
			out += "TODO NEWOP"
		elif opcode%100 == 8:
			out += "TODO NEWOP"
		elif opcode%100 == 99:
			out+= "!HALT!"
		else:
			print("wtf")
		out+=" "
		if opcode%100 in self.ARG_OP:
			out += self.__parse_log_arg(entry)
		elif opcode&100 in self.IMM_OP:
			out += self.__parse_log_imm(entry)
		return out
	
	def __parse_log_arg(self,entry:tuple):
		#0 -> address
		#1 -> instr
		#2 -> firstarg
		#3 -> secondarg
		#4 -> storeloc
		#5 -> memoryval of firstarg at exec
		#6 -> memoryval of secarg at exec
		opstring = ("+","*")[entry[1]%10 == 2]
		out = ""
		instr = entry[1]
		first_is_imm = int(instr/100) %10== 1
		sec_is_imm = int(instr/1000)%10==1
		thr_is_imm = int(instr/10000)%10 ==1
		if(thr_is_imm):
			print("nononono")
		
		val1 = -1
		val2 = -1
		if(first_is_imm):
			val1 = entry[2]
		else:
			val1 = entry[5]
		if(sec_is_imm):
			val2 = entry[3]
		else:
			val2 = entry[6]

		out += f"{val1} {opstring} {val2} = {self.__getres(opstring,val1,val2)} "


		out += f"store at self.memory[{entry[4]}]"
		return out

	def __parse_log_imm(self,entry:tuple):
		return ""
	def __getres(self,opstring,val1,val2):
		if opstring == "+":
			return val1+val2
		else:
			return val1*val2


			
