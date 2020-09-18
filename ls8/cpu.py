class CPU:
    """
    Main CPU class
    """

    def __init__(self):
        """
        Constructor
        """

        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True
        self.flag = [0] * 8

        self.table = {
            HLT : self.HLT,
            PRN : self.PRN,
            LDI : self.LDI,
            CMP : self.CMP,
            JMP : self.JMP,
            JE : self.JE,
            JNE : self.JNE,
            MUL : self.MUL,
            ADD : self.ADD,
            PUSH : self.PUSH,
            POP : self.POP,
            CALL : self.CALL,
            RET : self.RET,

        }

    
    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR 

    def load(self):
        """
        Load program into memory
        """
        pass
    
    def trace(self):
        """
        Prints out CPU state if debugging
        """
        pass

    def alu(self, op, operand_a, operand_b):
        """
        ALU operations.
        """

        if op == "ADD":
            self.reg[operand_a] += self.reg[operand_b]
        elif op == "MUL":
            self.reg[operand_a] *= self.reg[operand_b]
        elif op == "SUB":
            self.reg[operand_a] -= self.reg[operand_b]
        elif op == "CMP":
            if operand_a == operand_b:
                self.flag[E] = 0b00000001 # yes/true
            else:
                self.flag[E] = 0b00000000 # no/false
        
        else:
            raise Exception("Unsupported ALU operation.")

    def LDI(self, operand_a, operand_b):
        """
        Set the value of a register equal to an integer
        """
        self.reg[operand_a] = operand_b

    def HLT(self, operand_a, operand_b):
        """
        Halt CPU
        """
        self.running = False

    def PRN(self, operand_a, operand_b):
        """
        Print the decimal integer stored in given register
        """
        print(self.reg[operand_a])

    def CMP(self, operand_a, operand_b):
        """
        Compare values in two registers

        - if A = B, set `E` flag to 1, otherwise set it to 0
        - if A < B, set `L` flag to 1, otherwise set it to 0
        - if A > B, set `G` flag to 1, otherwise set it to 0
        """
        reg_num1 = self.reg[operand_a]
        reg_num2 = self.reg[operand_b]
        self.alu("CMP", reg_num1, reg_num2)

    def JMP(self, operand_a, operand_b):
        """
        Set PC to address in given register
        """
        self.pc = self.reg[operand_a]

    def JE(self, operand_a, operand_b):
        """
        If `Equal` flag is True, jump to address stored in register
        """
        if self.flag[E] == 0b00000001:
            self.pc = self.reg[operand_a]
        else:
            self.pc += 2

    def JNE(self, operand_a, operand_b):
        """
        If `E` flag is False or 0, jump to address stored in register
        """
        if self.flag[E] = 0b00000000:
            self.pc = self.reg[operand_a]
        else:
            self.pc += 2

    # ORIGINAL FUNCTIONS FROM SPRINT

    def MUL(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)

    def ADD(self, operand_a, operand_b):
        self.alu("ADD", operand_a, operand_b)

    def PUSH(self, operand_a, operand_b):
        # decrement stack
        self.reg[7] -= 1

        # grab val from reg
        reg_num = self.ram[self.pc + 1]
        value = self.reg[reg_num]

        # store on top of stack
        top_of_stack_addr = self.reg[SP]
        self.ram[top_of_stack_addr] = value

        self.pc += 2

    def POP(self, operand_a, operand_b):
        # increment stack
        value = self.ram_read(self.reg[SP])
        self.reg[operand_a] = value

        self.reg[SP] += 1
        self.pc += 2

    def CALL():
        pass

    def RET():
        pass

    def run():
        pass
