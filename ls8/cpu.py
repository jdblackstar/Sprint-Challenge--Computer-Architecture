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

    def PRN():
        pass

    def CMP():
        pass

    def JMP():
        pass

    def JE():
        pass

    def JNE():
        pass

    # ORIGINAL FUNCTIONS FROM SPRINT

    def MUL():
        pass

    def ADD():
        pass

    def PUSH():
        pass

    def POP():
        pass

    def CALL():
        pass

    def RET():
        pass

    def run():
        pass
