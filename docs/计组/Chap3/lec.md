# Chap3.Arithmetic for computer

??? "Introduction"

    <div align=center> ![1](1.png) </div>  

### Numbers

#### Signed and Unsigned Numbers  Possible Representations

![2](2.png)

* Sign Magnitude. Positive & Negative Zero **(Problem !)**
* One's Complement : 取反. Positive & Negative Zero **(Problem !)**
* Two's Complement : 取反+1. 

??? "Def"

    <div align=center> ![3](3.png) </div>  

> To know a negative num's definite value : **also invert and plus one**

**Biased notation**	

* `1000 0000` $=$ minimal negative value($-2^7$)		
* `0111 1111` $=$ maximal positive value ($2^7-1$)

![4](4.png)

**Sign Extention** `lbu`  vs. ` lb`

![5](5.png)



#### Operations

##### Operations

**Signed integer**

`slt` Set when less than

`slti` Set when less than immediate

**Unsigned integer**

`sltu` Set when less than

`sltiu` Set when less than immediate 

> "sltu"和"sltiu"都是MIPS汇编语言中的指令，但它们之间有一些重要的区别：
>
> **sltu**：
>
> - "sltu"代表"set less than unsigned"，用于无符号比较。
> - 它将两个寄存器中的无符号整数进行比较，如果第一个寄存器中的值小于第二个寄存器中的值，则结果为1；否则结果为0。
>
> **sltiu**：
>
> - "sltiu"代表"set less than immediate unsigned"，也用于无符号比较。
> - 与"sltu"类似，但是它将第一个寄存器中的值与一个立即数（常数）进行比较，而不是与另一个寄存器中的值进行比较。

??? "Example"

    <div align=center> ![6](6.png) </div>  

**New RISC V instructions**

* `lbu`  load byte unsigned : 

  Loads a byte into the lowest 8 bit of a register

  Fills the remaining bits with `0`

* `Lb` load byte (signed)

  Loads a byte into the lowest 8 bit of a register

  Extends the highest bit into the remaining 24 bits

* `sltu`: set on less than unsigned
* `slti`:  set on less than immediate
* `sltiu`: set on less than unsigned immediate

**Logical Operations**

![9](9.png)

## Arithmetic

### Addition & subtraction

#### Overflow

* $XOR$​ **Most significant bit** `^` **Carry bit**
* Actually we should $[MSB$`^`$Carry] and \ Operation_{add\ or\ sub}$

![7](7.png)

![8](8.png)

* Overflows in signed arithmetic instructions cause exceptions:

  `addadd immediate (addi)`

  `subtract (sub)`

* Overflows in unsigned arithmetic instructions don’t cause exceptions

  `add unsigned (addu)`

  `add immediate unsigned (addiu)`

  `Subtract unsigned (subu)`

### Constructing an ALU

* Half Adder:

   $S=X\oplus Y\\  C=XY$

* Full Adder :

  $Sum = X\oplus Y\oplus Carry_{in}$​ 

  $Carry_{out} = XY +(X+Y)Carry_{in}$​

  >  $X\oplus Y$ only different from $X+Y$ when $XY=1$ 

![10](10.png)

#### Overflow Detection

* Overflow V = $C_n\oplus C_{n-1}$

![11](11.png)

![12](12.png)

![13](13.png)

```verilog
module alu(A, B, ALU_operation, res, zero, overflow );
    input [31:0] A, B;
    input [2:0] ALU_operation;
    output [31:0] res;
    output zero, overflow ;
    wire [31:0] res_and,res_or,res_add,res_sub,res_nor,res_slt;
    reg [31:0] res;
    parameter one = 32'h00000001, zero_0 = 32'h00000000;
       assign res_and = A&B;
	 assign res_or = A|B;
	 assign res_add = A+B;
	 assign res_sub = A-B;
	 assign res_slt =(A < B) ? one : zero_0;
	 always @ (A or B or ALU_operation)
        	case (ALU_operation)
            	3'b000: res=res_and;	
            	3'b001: res=res_or;	
            	3'b010: res=res_add;	
            	3'b110: res=res_sub;	
	      	3'b100: res=~(A | B);
	      	3'b111: res=res_slt;
	      	default: res=32'hx;
        	endcase
	 assign zero = (res==0)? 1: 0;
endmodule
```

* Overflow code ?
* What is the difference The codes in the Synthesize?

#### Speed up

$P_i = A_i\oplus B_i \ \ \ \ G_i = A_iB_i$​

$S_i = P_i\oplus C_i\ \ \ \ C_{i+1} = G_i + P_iC_i$​​

![18](18.png)

??? "Improvement -- Reduce FAN-OUT"

    <div align=center>![14](14.png)![15](15.png) ![16](16.png)![17](17.png) </div>  



#### Carry Skip Adder

![19](19.png)

![20](20.png)

![32](32.png)

#### Carry Select Adder (CSA)

![21](21.png)

> Already caclulate(parallel) different situations,once the $C_0$​ is delivered, the result can be output.

![33](33.png)

![34](34.png)

### Multiplexer

Look at current bit position

* If multiplier is $1$ then add multiplicand Else add 0
* shift multiplicand left by 1 bit

![22](22.png)

??? "Multiplexter V1"

    <div align=center>![23](23.png)![24](24.png) </div>  

??? "Multiplexter V2"

    <div align=center>![25](25.png)![26](26.png)![27](27.png)![35](35.png) </div>  

??? "Multiplexter V3"

    <div align=center>![29](29.png)![30](30.png)![31](31.png)![28](28.png) </div>  

#### Booth's Algorithm

![37](37.png)

**Idea:** 

* If you have a sequence of `1s` subtract at first `'1'` in multiplier
* shift for the sequence of `'1s'`
* add where prior step had last `'1‘`

**Action**

* `1` `0` : subtract multiplicand from left
* `1` `1`  no arithmetic operation
* `0` `1`   add multiplicand to left half
* `0` `0` no arithmetic operation

$Bit_{-1} = 0$

**Arithmetic shift right:**

* keeps the leftmost bit constant
* no change of sign bit !

![38](38.png)

![39](39.png)

* 仍然是放在左边一路右移
* 注意signed shift right
* least significant bit初始加个零

### Division

??? "Division V1"

    <div align=center>![40](40.png)![41](41.png)![42](42.png) </div>  

* Reduction of Divisor and ALU width by half
* Shifting of the remainderSaving 1 iteration

??? "Division V2"

    <div align=center>![43](43.png) </div>  

??? "Division V3"

    <div align=center>![44](44.png)![45](45.png)![46](46.png)
    
    4.1 已经结束了除法操作，此时的高位就是我们的余数，但是这最后一次的结果还没有放回到 Reminder 中，因此我们需要再往左移一位为商留出空间，放入后，再把高位余数往右移动以抵消影响
    </div>  

#### Signed division

![47](47.png)

* 除零会产生溢出，由软件检测

## Floating point numbers

Standardized format  **IEEE 754**

* Single precision `8 bit exp, 23 bit significant`
* Double precision `11 bit exp, 52 bit significant`
* Both formats are supported by MIPS

![48](48.png)

* Leading '1' bit of significand  is implicit

- M: 尾数. 即默认`.xxx`是`1.xxx`(因为科学计数法，没有`0.xxx`)

- Exponent is biased(移码)

  Bias 127 for single precision

  Bias 1023 for double precision

  Have to be transfered back,but treated like unsigned inside



**NOTE** :$(-1)^{sign} • (1 + significand) • 2^{exponent - bias}$​

#### Limitations

**Overflow:**  &. **Underflow**

![49](49.png)

![50](50.png)

??? "EXAMPLE"

    <div align=center>![51](51.png) </div>  

#### Floating Point Addition

* Alignment
* The proper digits have to be added
* Addition of significant
* Normalization of the result  [重新规格化]
* Rounding

![52](52.png)

??? "EXAMPLE"

    <div align=center>![53](53.png) </div>  

![54](54.png)

#### Floating Point multiplication

![55](55.png)

> Algorithm

* Add exponents - bias

* Multiply the significands

  

* Normalize

* Over- underflow

* Rounding

* Sign

![56](56.png)

![57](57.png)

#### float devision

* Subtraction of exponents
* Division of the significants
* Normalisation
* Rounding
* Sign

