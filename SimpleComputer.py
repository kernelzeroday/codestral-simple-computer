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
        elif opcode == 0x2:  # SUB operation
            self.registers[dest_reg] = self.registers[regA] - self.registers[regB]
        elif opcode == 0x3:  # AND operation
            self.registers[dest_reg] = self.registers[regA] & self.registers[regB]
        elif opcode == 0x4:  # OR operation
            self.registers[dest_reg] = self.registers[regA] | self.registers[regB]
        elif opcode == 0x5:  # XOR operation
            self.registers[dest_reg] = self.registers[regA] ^ self.registers[regB]
        elif opcode == 0x6:  # JMP operation
            return regA
        elif opcode == 0x7:  # JZ operation
            if self.registers[dest_reg] == 0:
                return regA
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

class SimpleFloppyDrive:
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
            self.mmu.deallocate(start=self.current_start_address, size=file_size)
            # Simulate unloading the file from memory (in a real scenario, this would involve freeing up the memory)
            self.current_file = None
            self.current_start_address = None
        except Exception as e:
            print(f"Error unloading file: {e}")

class SimpleHardDrive:
    def __init__(self, mmu):
        self.mmu = mmu  # Reference to the MMU object
        self.current_partition = None  # The currently loaded partition on the hard drive
        self.current_start_address = None  # The start address of the current partition in memory

    def load(self, partition, file_size):
        """Load a partition from the hard drive into memory."""
        if self.current_partition is not None:
            print("Error: A partition is already loaded.")
            return
        try:
            start_address = self.mmu.allocate(file_size)
            # Simulate loading the file into memory (in a real scenario, this would involve reading from the hard drive)
            self.current_partition = partition  # Replace with actual partition name or identifier
            self.current_start_address = start_address
        except Exception as e:
            print(f"Error loading partition: {e}")

    def unload(self):
        """Unload the current partition from memory."""
        if self.current_partition is None:
            print("No partition loaded.")
            return
        try:
            file_size = 1024  # Replace with the actual file size
            self.mmu.deallocate(start=self.current_start_address, size=file_size)
            # Simulate unloading the partition from memory (in a real scenario, this would involve freeing up the memory)
            self.current_partition = None
            self.current_start_address = None
        except Exception as e:
            print(f"Error unloading partition: {e}")

class SimpleNetworkDevice:
    def __init__(self, mmu):
        self.mmu = mmu  # Reference to the MMU object
        self.connected_devices = []  # List of connected devices

    def connect(self, device):
        """Connect a device to this network device."""
        self.connected_devices.append(device)

    def disconnect(self, device):
        """Disconnect a device from this network device."""
        if device in self.connected_devices:
            self.connected_devices.remove(device)

    def send(self, data, destination_device):
        """Send data to another connected device."""
        if destination_device not in self.connected_devices:
            print("Error: Destination device is not connected.")
            return
        try:
            # Allocate memory for the data and simulate sending it to the destination device
            start_address = self.mmu.allocate(len(data))
            # Deallocate the memory after sending the data (in a real scenario, this would involve freeing up the memory)
            self.mmu.deallocate(start=start_address, size=len(data))
        except Exception as e:
            print(f"Error sending data: {e}")

class SimpleComputer:
    def __init__(self):
        self.cpu = SimpleCPU()
        self.gpu = SimpleGPU()
        self.mmu = SimpleMMU()
        self.floppy_drive = SimpleFloppyDrive(self.mmu)

    def load_program(self, program):
        self.floppy_drive.load(file_size=len(program))
        for i, instruction in enumerate(program):
            self.cpu.memory[self.floppy_drive.current_start_address + i] = instruction

    def run_program(self):
        for i in range(len(self.cpu.memory)):
            instruction = self.cpu.memory[i]
            if instruction == 0:  # End of program
                break
            self.cpu.run(instruction)

    def display_output(self):
        self.gpu.clear()
        # Display the output from the CPU (e.g., draw pixels on the screen)
        self.gpu.display()


class SimpleMIMDProcessor:
    def __init__(self, mmu, num_cores):
        self.mmu = mmu  # Reference to the MMU object
        self.num_cores = num_cores  # Number of cores in the processor
        self.cores = [SimpleCPU() for _ in range(self.num_cores)]  # List of CPU cores
    
    def load_programs(self, programs):
        """Load multiple programs onto the MIMD processor."""
        if len(programs) > self.num_cores:
            print("Error: Too many programs for available cores.")
            return
        try:
            for i, program in enumerate(programs):
                start_address = self.mmu.allocate(len(program))
                # Simulate loading the program into memory (in a real scenario, this would involve reading from storage)
                for j, instruction in enumerate(program):
                    self.cores[i].memory[start_address + j] = instruction
        except Exception as e:
            print(f"Error loading programs: {e}")

    def run_programs(self):
        """Run multiple programs on the MIMD processor simultaneously."""
        for i in range(self.num_cores):
            self.run_core(i)

    def run_core(self, core_index):
        """Run a single program on a specific CPU core."""
        cpu = self.cores[core_index]
        for i in range(len(cpu.memory)):
            instruction = cpu.memory[i]
            if instruction == 0:  # End of program
                break
            cpu.run(instruction)

