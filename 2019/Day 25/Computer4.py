class Computer:
    IMM_OP = (3, 4, 9)
    ARG_OP = (1, 2, 7, 8)
    JMP_OP = (5, 6)
    DEBUG = False
    instr_log = []

    def __init__(self, fName):
        self.fname = fName
        self.memory = {}
        self._readInput()
        self.printcount = 0
        self.instr_pointer = 0
        self.relative_base = 0
        self.new_line_started = True
        self.input_queue = []

    def reset(self):
        self.input_queue = []

        self.new_line_started = True
        self.relative_base = 0
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
            try:
                a = self.memory[self.instr_pointer + 1]
            except KeyError:
                a = 0
                self.memory[self.instr_pointer + 1] = 0
            try:
                b = self.memory[self.instr_pointer + 2]
            except KeyError:
                b = 0
                self.memory[self.instr_pointer + 2] = 0
            try:
                c = self.memory[self.instr_pointer + 3]
            except KeyError:
                c = 0
                self.memory[self.instr_pointer + 3] = 0
            addr_offset = 0
            try:
                if mode_first == 0 and op_code != 3:
                    a = self.memory[a]
                elif mode_first == 2 and op_code != 3:
                    a = self.memory[a + self.relative_base]
            except KeyError:
                if mode_first == 0:
                    self.memory[a] = 0
                    a = 0
                elif mode_first == 2:
                    self.memory[a + self.relative_base] = 0
                    a = 0
            try:
                if mode_second == 0:
                    b = self.memory[b]
                elif mode_second == 2:
                    b = self.memory[b + self.relative_base]
            except KeyError:
                if mode_second == 0:
                    self.memory[b] = 0
                    b = 0
                elif mode_second == 2:
                    self.memory[b + self.relative_base] = 0
                    b = 0

            if mode_third == 2 or (mode_first == 2 and op_code == 3):
                addr_offset = self.relative_base

            if op_code in self.IMM_OP:

                self.instr_log.append(
                    (self.instr_pointer, instr, self.memory[self.instr_pointer + 1])
                )

                self._do_op_imm(op_code, a, addr_offset)
                addr_offset = 0
                self.instr_pointer += 2

            elif op_code in self.JMP_OP:
                self._do_op_jmp(op_code, a, b)
            elif op_code in self.ARG_OP:
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

                self._do_op_arg(op_code, a, b, c, addr_offset)
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

    def _do_op_arg(
        self,
        op_code: int,
        first_arg: int,
        sec_arg: int,
        res_address: int,
        addr_offset: int,
    ):

        res_address += addr_offset

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

    def _do_op_imm(self, op_code: int, arg: int, addrOffset):
        if op_code == 3:  # read input
            arg += addrOffset
            if len(self.input_queue):
                self.memory[arg] = self.input_queue.pop(0)
            else:
                val = input("give input: ").strip()
                for i in range(1, len(val)):
                    self.input_queue.append(int(ord(val[i])))
                self.input_queue.append(10)
                self.memory[arg] = ord(val[0])
        elif op_code == 4:  # print
            self.printcount += 1
            end = ""
            # if arg == 0: end = "\r"
            arg_parsed = chr(arg)
            if self.new_lineinv_started:
                print(
                    f"[IntComp] {str(self.printcount).ljust(3)}>\t{arg_parsed}", end=end
                )
                self.new_line_started = False
            else:
                print(arg_parsed, end=end)
            if arg == 10:
                self.new_line_started = True

        elif op_code == 9:
            self.relative_base += arg
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
