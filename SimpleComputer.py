class SimpleCPU:
    def __init__(self):
        self.registers = [0] * 16  # 16 general-purpose registers
        self.memory = [0] * 256   # 256 memory locations

    def fetch(self, instruction_addr):
        return self.memory[instruction_addr]

    def decode(self, instruction):
        opcode = (instruction >> 12) & 0xF
        regA = (instruction >> 8) & 0xF
        regB = (instruction >> 4) & 0xF
        dest_reg = instruction & 0xF
        return opcode, regA, regB, dest_reg

    def execute(self, opcode, regA, regB, dest_reg):
        if opcode == 0x1:  # ADD operation
            self.registers[dest_reg] = self.registers[regA] + self.registers[regB]
        else:
            raise ValueError(f"Invalid opcode {opcode}")

    def run(self, instruction):
        instruction_addr = 0
        self.memory[instruction_addr] = instruction
        opcode, regA, regB, dest_reg = self.decode(self.fetch(instruction_addr))
        self.execute(opcode, regA, regB, dest_reg)
class SimpleGPU:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.frame_buffer = [[(0, 0, 0)] * width for _ in range(height)]

    def clear(self, color=(0, 0, 0)):
        self.frame_buffer = [[color] * self.width for _ in range(self.height)]

    def draw_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.frame_buffer[y][x] = color

    def display(self):
        for row in self.frame_buffer:
            print(" ".join([f"\033[48;2;{r};{g};{b}m  \033[0m" for r, g, b in row]))
class SimpleMMU:
    def __init__(self, memory_size=1024):
        self.memory = [0] * memory_size  # Initialize memory with all zeros
        self.memory_size = memory_size
        self.free_memory = memory_size

    def allocate(self, size):
        if self.free_memory < size:
            raise MemoryError("Not enough free memory")
        for i in range(len(self.memory)):
            if all(m == 0 for m in self.memory[i:i+size]): # Find a block of free memory
                for j in range(i, i+size):
                    self.memory[j] = 1  # Mark the memory as allocated
                self.free_memory -= size
                return i
        raise MemoryError("Something went wrong during allocation")

    def deallocate(self, start, size):
        for i in range(start, start+size):
            if self.memory[i] != 1:
                raise ValueError("Memory at this address is not allocated")
            self.memory[i] = 0  # Mark the memory as free
        self.free_memory += size            


