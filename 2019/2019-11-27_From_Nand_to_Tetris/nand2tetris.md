# From Nand to Tetris

![course](img/course.png)

[From Nand to Tetris - Building a Modern Computer From First Principles](https://www.nand2tetris.org/)

- [From Nand to Tetris](#from-nand-to-tetris)
  - [Part 1](#part-1)
  - [Project 1: Boolean Logic](#project-1-boolean-logic)
  - [Project 2: Boolean Arithmetic - ALU](#project-2-boolean-arithmetic---alu)
  - [Project 3: Sequential Logic - Memory](#project-3-sequential-logic---memory)
  - [Project 4: Machine Language](#project-4-machine-language)
  - [Project 5: Computer Architecture](#project-5-computer-architecture)
  - [Project 6: Assembler](#project-6-assembler)
  - [Project 7: VM I: Stack Arithmetic](#project-7-vm-i-stack-arithmetic)
  - [Project 8: VM II: Program Control](#project-8-vm-ii-program-control)
  - [Project 9: High-Level Language](#project-9-high-level-language)
  - [Project 10: Compiler I: Syntax Analysis](#project-10-compiler-i-syntax-analysis)
  - [Project 11: Compiler II: Code Generation](#project-11-compiler-ii-code-generation)
  - [Project 12: Operating System](#project-12-operating-system)
  - [refs](#refs)

## Part 1

![part1](img/part1.png)

## Project 1: Boolean Logic

![gate](img/gate.png)

## Project 2: Boolean Arithmetic - ALU

![alu0](img/alu0.png)  
![alu1](img/alu1.png)  
<!-- ![alu2](img/alu2.png)   -->
![alu3](img/alu3.png)  

## Project 3: Sequential Logic - Memory

- flip-flop -  触发器（延时器）
- 1-bit register - 寄存器
- Multi-bit register
- Random Access Memory (RAM) - 内存
- Counter - 计数器

![flip-flop](img/flip-flop.png)  
![1-bit register](img/1-bit_register.png)  
![register](img/register.png)  
![RAM](img/RAM.png)  
![Counter](img/counter.png)  

## Project 4: Machine Language

![concept](img/concept.png)  
![a-c](img/a-c.png)  
![a-instruction](img/a-instruction.png)  
![c-instruction](img/c-instruction.png)  
![c-symbolic](img/c-symbolic.png)  
![iterative](img/iterative.png)  
![input](img/input.png)  

## Project 5: Computer Architecture

- von Neumann Architecture

![von-arch](img/von-arch.png)

- Harvard Architecture

![harvard-arch](img/harvard.png)

- Hack Computer

![hack](img/hack.png)

- CPU

![cpu](img/cpu.png)

- `instruction`
  - `A-instruction`: an address value, that should be recorded in A-register
  - `C-instruction`: a command, that controls the procession
- `A-register`: recording the address value
- `D-register`: storing the calculated value
- `ALU`: calculating

next, examples for handling instructions

- a-instructions

![a-instructions](img/handling_a-instructions.png)

- c-instructions

![c-instructions](img/handling_c-instructions.png)

- pc - control

![pc](img/pc.png)

we've built Hack Computer

- Hardware projects

![hardware-projects](img/hardware-projects.png)

## Project 6: Assembler

- Assembly process

![asm_process](img/asm_process.png)

- Symbol table

![symbol_table](img/symbol_table.png)

- Translating A-instructions

![trans_a-instructions](img/trans_a-instructions.png)

- Translating C-instructions

![trans_c-instructions](img/trans_c-instructions.png)

## Project 7: VM I: Stack Arithmetic

![part2](./img/part2.png)

![high_to_low](./img/hight_to_low.png)

![memory_segments](./img/memory_segments.png)

![vm_mapping_1](./img/vm_mapping_1.png)

![vm_mapping_2](./img/vm_mapping_2.png)

![p7p8](./img/p7p8.png)




## Project 8: VM II: Program Control
## Project 9: High-Level Language
## Project 10: Compiler I: Syntax Analysis
## Project 11: Compiler II: Code Generation
## Project 12: Operating System


## refs
- [Richard Feynman: Computer Heuristics](https://sites.google.com/site/principiascientifica/lecture/richard-feynman-computer-heuristics)