# SimpleComputer Demo

This demo showcases the basic functionalities of the `SimpleComputer` system, which includes a CPU, GPU, and MMU. Below is a quick explanation of the demo code and how it utilizes these components.

## Components

### 🧠 SimpleCPU
The `SimpleCPU` class is responsible for executing instructions. It has:
- **Registers**: 16 general-purpose registers.
- **Memory**: 256 memory locations.
- **Methods**:
  - `fetch(instruction_addr)`: Fetches an instruction from memory.
  - `decode(instruction)`: Decodes the fetched instruction into opcode and registers.
  - `execute(opcode, regA, regB, dest_reg)`: Executes the decoded instruction.
  - `run(instruction)`: Runs a single instruction by fetching, decoding, and executing it.

### 🎨 SimpleGPU
The `SimpleGPU` class handles graphical operations. It has:
- **Frame Buffer**: A 2D array representing the screen.
- **Methods**:
  - `clear(color)`: Clears the frame buffer with the specified color.
  - `draw_pixel(x, y, color)`: Draws a pixel at the specified coordinates with the given color.
  - `display()`: Displays the current frame buffer.

### 🗄️ SimpleMMU
The `SimpleMMU` class manages memory allocation. It has:
- **Memory**: An array representing the memory.
- **Methods**:
  - `allocate(size)`: Allocates a block of memory of the specified size.
  - `deallocate(start, size)`: Deallocates a block of memory starting at the specified address.

## Demo Code

### CPU Operations
1. **Initialize CPU**: Create an instance of `SimpleCPU`.
2. **Set Registers**: Set initial values in registers.
3. **Encode Instruction**: Encode an 'ADD' instruction to add values in two registers and store the result in another register.
4. **Run Instruction**: Execute the encoded instruction.
5. **Check Result**: Print the result stored in the destination register.

### GPU Operations
1. **Initialize GPU**: Create an instance of `SimpleGPU` with a specified width and height.
2. **Clear Frame Buffer**: Clear the frame buffer with a black color.
3. **Draw Pixels**: Draw a red square on the frame buffer.
4. **Display Frame Buffer**: Display the rendered image.

### MMU Operations
1. **Initialize MMU**: Create an instance of `SimpleMMU` with a specified memory size.
2. **Allocate Memory**: Allocate a block of memory.
3. **Print Allocation**: Print the start and end addresses of the allocated memory.
4. **Deallocate Memory**: Deallocate the previously allocated memory.
5. **Print Deallocation**: Print a message indicating that the memory has been deallocated.

For more details, refer to the [SimpleCPU](#simplecpu), [SimpleGPU](#simplegpu), and [SimpleMMU](#simplemmu) classes in the `SimpleComputer.py` file.
