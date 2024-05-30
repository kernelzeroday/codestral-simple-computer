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

class simpleFloppyDrive:
    def __init__(self, mmu):
        self.mmu = mmu  # Reference to the MMU object
        self.current_file = None  # The currently loaded file
        self.current_start_address = None  # The start address of the current file in memory

    def load(self, file_size):
        """Load a file from the floppy drive into memory."""
        if self.current_file is not None:
            print("Error: A file is already loaded.")
            return
        try:
            start_address = self.mmu.allocate(file_size)
            # Simulate loading the file into memory (in a real scenario, this would involve reading from the floppy drive)
            self.current_file = "<filename>"  # Replace with actual filename
            self.current_start_address = start_address
        except Exception as e:
            print(f"Error loading file: {e}")

    def unload(self):
        """Unload the current file from memory."""
        if self.current_file is None:
            print("No file loaded.")
            return
        try:
            file_size = 1024  # Replace with the actual file size
            self.mmu.deallocate(start=self.current_start_address, size=(self.current_start_address + file_size - 1))
            # Simulate unloading the file from memory (in a real scenario, this would involve freeing up the memory)
            self.current_file = None
            self.current_start_address = None
        except Exception as e:
            print(f"Error unloading file: {e}")
