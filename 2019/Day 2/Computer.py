class Computer:
    def __init__(self, fName):
        self.fname = fName
        self.workArray = []
        self.readInput()

    def reset(self):
        self.workArray = self.__reset_array[:]

    def readInput(self):
        arr_of_strings = open(self.fname).read().split(",")
        for i in range(0, len(arr_of_strings)):
            self.workArray.append(int(arr_of_strings[i]))

        self.__reset_array = self.workArray[:]

    def get(self, index):
        return self.workArray[index]

    def set(self, index, value):
        self.workArray[index] = value

    def work(self):
        op_index = 0
        iter_count = 0
        while self.workArray[op_index] != 99:
            iter_count += 1
            op_code = self.workArray[op_index]
            val1_indx = self.workArray[op_index + 1]
            val2_indx = self.workArray[op_index + 2]
            res_indx = self.workArray[op_index + 3]
            self.do_operation(op_code, val1_indx, val2_indx, res_indx)
            op_index += 4
        # print("ended computation on index",op_index," after ",iter_count," steps")

    def do_operation(
        self, op_code: int, val1_indx: int, val2_indx: int, res_indx: int, verbose=False
    ):
        if verbose:
            print(
                f"got opCode {op_code}, val1 index {val1_indx}(={self.workArray[val1_indx]}), val2 index {val2_indx}(={self.workArray[val2_indx]}) and res index {res_indx} "
            )
        val1 = self.workArray[val1_indx]
        val2 = self.workArray[val2_indx]
        if op_code == 1:
            self.workArray[res_indx] = val1 + val2
            if verbose:
                print(
                    f"put result of {val1} + {val2} (={val1+val2}) at index {res_indx} [check: {self.workArray[res_indx]}]"
                )
        elif op_code == 2:
            self.workArray[res_indx] = val1 * val2
            if verbose:
                print(
                    f"put result of {val1} * {val2} (={val1*val2}) at index {res_indx} [check: {self.workArray[res_indx]}]"
                )
        else:
            raise ValueError("illegal opcode >" + op_code + "< found!")
