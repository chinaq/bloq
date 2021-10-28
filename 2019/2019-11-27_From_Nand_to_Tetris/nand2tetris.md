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
  - [Part 2](#part-2)
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

![gate](img/01/gate.png)



## Project 2: Boolean Arithmetic - ALU

![alu0](img/02/alu0.png)  
![alu1](img/02/alu1.png)  
![alu3](img/02/alu3.png)  



## Project 3: Sequential Logic - Memory

- flip-flop -  触发器（延时器）
- 1-bit register - 寄存器
- Multi-bit register
- Random Access Memory (RAM) - 内存
- Counter - 计数器

![flip-flop](img/03/flip-flop.png)  
![1-bit register](img/03/1-bit_register.png)  
![register](img/03/register.png)  
![RAM](img/03/RAM.png)  
![Counter](img/03/counter.png)  



## Project 4: Machine Language

![concept](img/04/concept.png)  
![a-c](img/04/a-c.png)  
![a-instruction](img/04/a-instruction.png)  
![c-instruction](img/04/c-instruction.png)  
![c-symbolic](img/04/c-symbolic.png)  
![iterative](img/04/iterative.png)  
![input](img/04/input.png)  



## Project 5: Computer Architecture

- von Neumann Architecture

![von-arch](img/05/von-arch.png)

- Harvard Architecture

![harvard-arch](img/05/harvard.png)

- Hack Computer

![hack](img/05/hack.png)

- CPU

![cpu](img/05/cpu.png)

- `instruction`
  - `A-instruction`: an address value, that should be recorded in A-register
  - `C-instruction`: a command, that controls the procession
- `A-register`: recording the address value
- `D-register`: storing the calculated value
- `ALU`: calculating

next, examples for handling instructions

- a-instructions

![a-instructions](img/05/handling_a-instructions.png)

- c-instructions

![c-instructions](img/05/handling_c-instructions.png)

- pc - control

![pc](img/05/pc.png)

we've built Hack Computer

- Hardware projects

![hardware-projects](img/05/hardware-projects.png)



## Project 6: Assembler

- Assembly process

![asm_process](img/06/asm_process.png)

- Symbol table

![symbol_table](img/06/symbol_table.png)

- Translating A-instructions

![trans_a-instructions](img/06/trans_a-instructions.png)

- Translating C-instructions

![trans_c-instructions](img/06/trans_c-instructions.png)


## Part 2

![part2](./img/part2.png)


## Project 7: VM I: Stack Arithmetic

![high_to_low](./img/07/hight_to_low.png)

![memory_segments](./img/07/memory_segments.png)

![this_that_0](./img/07/this_that_0.png)

![this_that_1](./img/07/this_that_1.png)

![vm_mapping_1](./img/07/vm_mapping_1.png)

![vm_mapping_2](./img/07/vm_mapping_2.png)

![p7p8](./img/07/p7p8.png)



## Project 8: VM II: Program Control

- Branching
  - goto label
  - if-goto label
  - label

![goto](./img/08/goto.png)

- Function View

![function_state](./img/08/function_state.png)

![vm_executing](./img/08/vm_executing.png)

![function_call_return](./img/08/function_call_return.png)

- Function
  - call
  - function
  - return

![call](./img/08/call.png)

![function](./img/08/function.png)

![return](./img/08/return.png)


- vm done

![vm_done](./img/08/vm_done.png)

- global

![booting](./img/08/booting.png)

![vm_mapping_3](./img/08/vm_mapping_3.png)




## Project 9: High-Level Language

![high_level_language](img/09/high_level_language.jpg)

![p9_target](img/09/p9_target.jpg)

![jack_example](img/09/jack_example.jpg)


## Project 10: Compiler I: Syntax Analysis

![parsing](img/10/parsing.jpg)

![two-tier](img/10/two_tier.jpg)

![road_map](img/10/road_map_token.jpg)

![token_example](img/10/token_example.jpg)

## Project 11: Compiler II: Code Generation

![code_generation](img/11/code_generation.jpg)

![road_map](img/11/road_map_vm.jpg)

- example

![jack_to_vm](img/11/jack_to_vm.jpg)

- 挑战内容

![compilation_challenges](img/11/compilation_challenges.jpg)

- this & that
  - pointer 0 代表了 this，何时被重新写入
    - method 中间代码第一步为 push pointer 0 即把当前对象指针放入 pointer 0
    - 结束后回复原 pointer 0 值
    - this 的 heap 中其实仅包含了 field

    ![ram_this](img/11/ram_this.jpg)

  - pointer 1 代表了 that，数组

    ![this_that](img/11/ram_that.jpg)

## Project 12: Operating System

![sys](img/12/sys.jpg)

![os](img/12/os.jpg)


## refs
- [Richard Feynman: Computer Heuristics](https://sites.google.com/site/principiascientifica/lecture/richard-feynman-computer-heuristics)