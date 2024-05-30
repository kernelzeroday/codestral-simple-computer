from SimpleComputer import SimpleCPU, SimpleGPU, SimpleMMU, simpleFloppyDrive
cpu = SimpleCPU()

# Set up some initial values in registers
cpu.registers[1] = 5
cpu.registers[2] = 7

# Encode an 'ADD' instruction to add the values in registers 1 and 2, store the result in register 3
add_instruction = (0x1 << 12) | (1 << 8) | (2 << 4) | 3

cpu.run(add_instruction)

# Check the value in register 3 to see the result of the 'ADD' operation
result = cpu.registers[3]
print(result)

gpu = SimpleGPU(width=32, height=16)

# Clear the frame buffer with black color (default)
gpu.clear()

# Draw a red square at coordinates (5, 4) to (9, 8)
square_color = (255, 0, 0)
for y in range(4, 9):
    for x in range(5, 10):
        gpu.draw_pixel(x, y, square_color)

# Display the rendered image on the virtual frame buffer
gpu.display()

mmu = SimpleMMU(memory_size=4096)  # Create an MMU with 4KB of memory

# Allocate some memory for testing
test_size = 512  # For example, let's allocate 512 bytes of memory for a test
start_address = mmu.allocate(test_size)
print(f"Allocated memory from address {start_address} to {start_address + test_size - 1}")


# Deallocate the used memory
mmu.deallocate(start=start_address, size=test_size)
print("Memory deallocated")

mmu = SimpleMMU(memory_size=4096)  # Create an MMU with 4KB of memory
floppy = simpleFloppyDrive(mmu)  # Create a floppy drive that interacts with the MMU

# Load a file from the floppy drive into memory
file_size = 1024  # For example, let's load a file of size 1KB
floppy.load(file_size)
print(f"Loaded file {floppy.current_file} at address {floppy.current_start_address}")


# Unload the current file from memory
floppy.unload()
print("File unloaded")