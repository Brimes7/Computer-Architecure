"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.hlt = False

    def prn(self, address):
        print(self.register[address])


    def ram_read(self, meme):
        return self.ram[meme]

    def ram_write(self, meme, data):
        self.ram[meme] = data

    def mul(self, operand_a, operand_b):
        self.register[operand_a] = self.register[operand_a] * self.register[operand_b]

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        program_name = sys.argv[1]
        #Reading each file,
        #When it gets the file nd it no work it fails
        with open(program_name, "r") as file:
            for line in file:
                try:
                    instruction = int (line[:8], 2)
                    self.ram[address] = instruction
                    address += 1
                except ValueError:
                    pass
        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while self.hlt == False:
            instruction = self.ram[self.pc]
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)
            #LDI
            if instruction == 0b10000010:

                self.register[operand_a] = operand_b
                self.pc += 3
            #Print method
            if instruction == 0b01000111:
                self.prn(operand_a)
                self.pc += 2
            #instruction = bin(instruction)[6:]

            if instruction == 0b00000001:
                self.hlt = True
            #Multiply
            if instruction == 0b10100010:
                self.mul(operand_a, operand_b)
                self.pc+=3


cpu = CPU()
cpu.load()
cpu.run()



