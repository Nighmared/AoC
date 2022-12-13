class Computer:
    IMM_OP = (3, 4)
    ARG_OP = (1, 2, 7, 8)
    JMP_OP = (5, 6)
    DEBUG = False
    instr_log = []
    inval = -1

    def __init__(self, fName):
        self.fname = fName
        self.memory = {}
        self._readInput()
        self.printcount = 0
        self.instr_pointer = 0

    def reset(self):
        self.instr_pointer = 0
        self.printcount = 0
        self.instr_log.clear()
        self.memory = self.__reset_memory.copy()

    def _readInput(self):
        arr_of_strings = open(self.fname).read().split(",")
        for i in range(0, len(arr_of_strings)):
            self.memory[i] = int(arr_of_strings[i])

        self.__reset_memory = self.memory.copy()

    def get(self, index):
        return self.memory[index]

    def set(self, index, value):
        self.memory[index] = value

    def work(self):
        self.instr_pointer = 0
        instr = self.memory[self.instr_pointer]
        op_code = instr % 100
        print("******************************")
        while op_code != 99:
            mode_first = int(instr / 100) % 10  # C
            mode_second = int(instr / 1000) % 10  # B
            mode_third = int(instr / 10000) % 10  # A

            if op_code in self.IMM_OP:
                self.instr_log.append(
                    (self.instr_pointer, instr, self.memory[self.instr_pointer + 1])
                )
                a = self.memory[self.instr_pointer + 1]
                if mode_first == 0 and op_code != 3:
                    a = self.memory[a]
                self._do_op_imm(op_code, a)
                self.instr_pointer += 2
            elif op_code in self.JMP_OP:
                a = self.memory[self.instr_pointer + 1]
                b = self.memory[self.instr_pointer + 2]
                if mode_first == 0:
                    a = self.memory[a]
                if mode_second == 0:
                    b = self.memory[b]
                self._do_op_jmp(op_code, a, b)

            elif op_code in self.ARG_OP:
                a = self.memory[self.instr_pointer + 1]
                b = self.memory[self.instr_pointer + 2]
                c = self.memory[self.instr_pointer + 3]
                if mode_first == 0:
                    a = self.memory[a]
                if mode_second == 0:
                    b = self.memory[b]

                self.instr_log.append(
                    (
                        self.instr_pointer,
                        instr,
                        self.memory[self.instr_pointer + 1],
                        self.memory[self.instr_pointer + 2],
                        c,
                        a,
                        b,
                    )
                )

                self._do_op_arg(op_code, a, b, c)
                self.instr_pointer += 4
            else:
                print("===================\n oh no we got an error")
                print("heres some info")
                print(self.instr_pointer)
                print("\n")
                print(f"unknown opcode >{op_code}< found! ")
                return  # dont raise error cuz output gets uselessly messy

            instr = self.memory[self.instr_pointer]  # fetch next instr
            op_code = instr % 100  # get opcode
        print("******************************\n")

    def _do_op_jmp(self, op_code, first_arg, sec_arg):
        if op_code == 5:
            if first_arg != 0:
                self.instr_pointer = sec_arg
            else:
                self.instr_pointer += 3
        elif op_code == 6:
            if first_arg == 0:
                self.instr_pointer = sec_arg
            else:
                self.instr_pointer += 3
        else:
            raise ValueError("thats a nope from me...")

    def _do_op_arg(self, op_code: int, first_arg: int, sec_arg: int, res_address: int):
        if op_code == 1:
            self.memory[res_address] = first_arg + sec_arg
            if self.DEBUG:
                print(
                    f"stored {first_arg}+{sec_arg} = {first_arg+sec_arg} at self.memory[{res_address}] "
                )
        elif op_code == 2:
            self.memory[res_address] = first_arg * sec_arg
            if self.DEBUG:
                print(
                    f"stored  {first_arg}*{sec_arg} = {first_arg*sec_arg} at self.memory[{res_address}] "
                )
        elif op_code == 7:
            self.memory[res_address] = int(first_arg < sec_arg)
        elif op_code == 8:
            self.memory[res_address] = int(first_arg == sec_arg)
        else:
            raise ValueError("wtf this shouldnt be possible lol")

    def _do_op_imm(self, op_code: int, arg: int):
        if op_code == 3:  # read input
            if self.inval == -1:
                val = int(input("give input: "))
                self.memory[arg] = val
            else:
                print(f"give input: {self.inval}")
                self.memory[arg] = self.inval
            print()
        elif op_code == 4:  # print
            self.printcount += 1
            end = "\n"
            if arg == 0:
                end = "\r"
            print(f"[IntComp] {str(self.printcount).ljust(3)}>\t{arg}", end=end)
            if arg != 0 and abs(arg) < 10000:
                for i in range(min(10, len(self.instr_log)), 0, -1):
                    print(self.__parse_log_entry(self.instr_log[-i]))
        else:
            raise ValueError("neither should this be possible lol")

    def __parse_log_entry(self, entry: tuple) -> str:
        opcode = entry[1]
        instr_ad = entry[0]
        arg1s = entry[2:]
        out = ""
        out += str(instr_ad) + " =>\t"
        out += str(entry[1:])
        out += "\t"
        out += "#"
        if opcode % 100 == 1:
            out += "add"
        elif opcode % 100 == 2:
            out += "multiply"
        elif opcode % 100 == 3:
            out += "input"
        elif opcode % 100 == 4:
            out += "==================output"
        elif opcode % 100 == 5:
            out += "TODO NEWOP"
        elif opcode % 100 == 6:
            out += "TODO NEWOP"
        elif opcode % 100 == 7:
            out += "TODO NEWOP"
        elif opcode % 100 == 8:
            out += "TODO NEWOP"
        elif opcode % 100 == 99:
            out += "!HALT!"
        else:
            print("wtf")
        out += " "
        if opcode % 100 in self.ARG_OP:
            out += self.__parse_log_arg(entry)
        elif opcode & 100 in self.IMM_OP:
            out += self.__parse_log_imm(entry)
        return out

    def __parse_log_arg(self, entry: tuple):
        # 0 -> address
        # 1 -> instr
        # 2 -> firstarg
        # 3 -> secondarg
        # 4 -> storeloc
        # 5 -> memoryval of firstarg at exec
        # 6 -> memoryval of secarg at exec
        opstring = ("+", "*")[entry[1] % 10 == 2]
        out = ""
        instr = entry[1]
        first_is_imm = int(instr / 100) % 10 == 1
        sec_is_imm = int(instr / 1000) % 10 == 1
        thr_is_imm = int(instr / 10000) % 10 == 1
        if thr_is_imm:
            print("nononono")

        val1 = -1
        val2 = -1
        if first_is_imm:
            val1 = entry[2]
        else:
            val1 = entry[5]
        if sec_is_imm:
            val2 = entry[3]
        else:
            val2 = entry[6]

        out += f"{val1} {opstring} {val2} = {self.__getres(opstring,val1,val2)} "

        out += f"store at self.memory[{entry[4]}]"
        return out

    def __parse_log_imm(self, entry: tuple):
        return ""

    def __getres(self, opstring, val1, val2):
        if opstring == "+":
            return val1 + val2
        else:
            return val1 * val2
