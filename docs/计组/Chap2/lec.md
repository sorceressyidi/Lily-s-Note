<font face = 'Times New Roman'>

# Chap2:Language of the Computer(RISC V)

#### Instruction Characteristics
![1](1.png)
* 操作数位宽可以不同，可以是立即数/寄存器/内存
* Load/Store 结构
  * 指令分类：Load/Store结构将指令分为两类：加载（Load）指令和存储（Store）指令。这两类指令分别用于从内存中加载数据到寄存器或将寄存器中的数据存储到内存中
  * 数据传输：在Load/Store结构中，**只有**Load和Store指令能够直接访问内存。其他指令，如算术运算指令或逻辑指令，必须首先将数据加载到寄存器中，然后执行操作，最后再将结果存回内存
## Operations of the Computer Hardware

!!! Example
    * C code
    ``` C
    f = (g + h) - (i + j);
    ```
    * RISC-V code
    ``` C
    add t0, g, h
    add t1, i, j
    sub f, t0, t1
    ```

```assembly
;Not good for parallel opeartions
add t0, g, h
sub t0, t0, i
sub f, t0, j
```

### Regisers

* 32 registers in RISC-V
* 64 bits for each register in RISC-V

![2](2.png)

![3](3.png)

* 为什么内存是 $2^{61}$ 个 doublewords?  
  可以表示的地址有这么多，因为我们以 64 位寄存器为基址，可以表示的双字就是 $2^{64}/2^3=2^{61}$ (这里 $2^3$ 表示 8 个字节，即双字). 即我们的 `load` 指令可以访问的范围有这么大。 
* for `x0` : 因为经常有 0 参与计算，将其存在一个寄存器中，便于计算

```assembly
add x5,x20,x21
add x6,x22,x23
sub x19,x5,x6
```

### Memory Operands

Data transfer instructions
* Load: Load values from memory to register
* Store: Store result from register to memory; store doubleword

**Memory is *byte addressed*.**

* RISC-V is **Little Endian**  

    ![4](4.png)

* RISC-V dose not require words to be aligned in memory  : **To Save Memory**

  > words align: A word is 4 byte
  >
  > 我们要求字的起始地址一定要是 4 的倍数 : 访存更加方便

  ![5](5.png)

```assembly
LW t0,[0,4,8,...] 
LD t0,[0,8,16,32...]
```

#### Data Transfer instruction

* store 指令没有目的寄存器.
* Array are in the memory -- Stack.

??? "Example"

    <div align=center> ![6](6.png) ![7](7.png)![8](8.png)</div>  

```c
g = h + A[i]
//assume g,h,i - x18,x19,x20 base address of A -x22
```

* note `0(x5)` `x5` is for 偏移

```assembly
add x5,x20,x20
add x5,x5,x5
add,x5,x5,x5
add,x5,x5,x22
ld,x6,0(x5) 
add x18,x19,x6
```

### Registers vs. Memory

* Registers are faster to access than memory  
* Operating on memory data requires loads and stores  
* Compiler must use registers for variables as much as 
possible  
* Spilling Registers : putting less comonly used variables into memory

### Constant or Immediate Operands

**Immediate**: Other method for adding constant  

* Avoids the load instruction  

* Offer versions of the instruction   
  ***e.g.*** `addi x22, x22, 4`  

  ![9](9.png)  

* Design Principle 3 - Make the common case fast.  

## Representing Instructions in the Computer

??? "Translating assembly into machine instruction"

    <div align=center>![10](10.png)</div>  

### R-format instructions

![11](11.png)

* *opcode*: operaion code
* *rd*: destination register number
* *funct3*: 3-bit function code(additional opcode)   
eg. `load byte / load half`
* *rs1/rs2*: the first/second source register number
* *funct7*: 7-bit function code(additional opcode)

#### I-format Instructions

![12](12.png)

  * Immediate arithmetic and load instructions  

  ***e.g.*** `addi`, `ld`  

* *rs1*: source or base address register number

* *immediate*: constant operand, or offset added to base 
address  `将 rs2, funct7 合并了，得到 12 位立即数`

![13](13.png)

### S-format

![14](14.png)

* *rs1*: base address register number
* *rs2*: source opearand register number
* immediate:  Split so that *rs1* and *rs2* fields always in the same place.  

![15](15.png)

??? Example
    <div align=center> <img src="http://cdn.hobbitqia.cc/202303212250754.png" width = 60%/> </div>
    <div align=center> <img src="http://cdn.hobbitqia.cc/202303212251359.png" width = 60%/> </div>

**Stored Program Computer**  

![16](16.png)

* See Slides Trojan 密码窃取 拳击游戏

![17](17.png)

## Logical Operations

| Operation     | C    | Java | RISC-V      |
| :------------ | ---- | ---- | ----------- |
| Shift left    | <<   | <<   | `slli`      |
| Shift right   | >>   | >>>  | `srli`      |
| Bit-by-by AND | &    | &    | `and, andi` |
| Bit-by-by OR  | \|   | \|   | `or, ori`   |
| Bit-by-by XOR | ^    | ^    | `xor, xori` |
| Bit-by-by NOT | ~    | ~    | -           |

* note `0(x5)` `x5` is for 偏移

### Shift

<div align=center> <img src="http://cdn.hobbitqia.cc/202303212304867.png" width = 50%/> </div>  

* I 型指令
* 为什么还有 `funct6` : 移位不需要这么多立即数，只要六位 ($2^6=64$) 即可。
* 左移 i 位相当于乘 $2^i$, 右移 i 位相当于除 $2^i$.  

### AND

<div align=center> <img src="http://cdn.hobbitqia.cc/202303212308207.png" width = 50%/> </div>  

### OR

<div align=center> <img src="http://cdn.hobbitqia.cc/202303212309232.png" width = 50%/> </div>  

### XOR

<div align=center> <img src="http://cdn.hobbitqia.cc/202303212309740.png" width = 50%/> </div>  

* Useful for `not--xor 1111111...`

## Instructions for making decisions

### Branch instructions

​	



</font>