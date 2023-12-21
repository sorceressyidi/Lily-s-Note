## Memory Organization

* **Access is based on words as the access unit.**

### Basic Memory Operations

* Read Memory 

  <table>
    <tr>
      <td>Chip select</td>
      <td>Read/not Write</td>
      <td>memory operation</td>
    </tr>
    <tr>
      <td>0</td>
      <td></td>
      <td>None</td>
    </tr>
  	<tr>
      <td>1</td>
      <td>0</td>
      <td>Write to selected word</td>
    </tr>
  	<tr>
      <td>1</td>
      <td>1</td>
      <td>Read from selected word</td>
    </tr>
  </table>

* Write Memory

### Memory opertion timing

> 65ns -- 'read speed'--is critical for the whole speed.

![1](1.png)

## RAM

### Types of Random Access Memory

#### Static RAM -- Cell

**Information stored in Latches**

![3](3.png)

> Select = 0 **HOLD**
>
> Select = 1 **OUTPUT DATA**. 「**INPUT** depends on $B$ and $\bar{B}$」

![2](2.png)

* Bit select = 0 : **NO WRITING or READING** -- Bit Slice Disabled

* Word select : only one allowed to be **ONE**

* Bit select = 1:

  <table>
    <tr>
      <td>Read/not Write</td>
      <td>B</td>
      <td>not B</td>
      <td>Word select</td>
      <td>Result</td>
    </tr>
  	<tr>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>One piece of information stored in one<br> selected latch output </td>
    </tr> 
  	<tr>
      <td>0</td>
      <td>Data</td>
      <td>not Data</td>
      <td>1</td>
      <td>The input information is stored in the<br> one selected latch </td>
    </tr> 
  </table>

* $2^{n-1}$ Word using 1-Bit RAM IC

  ![4](4.png)

  Chip Select : When CS=0 Data Output 高阻态

##### Cell Arrays and Coincident Selection

* Uses two decoders, one for words and one for bits
* Word select becomes Row select
* Bit select becomes Column select

> 16x1

![5](5.png)

* Still one **ONE** chosen

##### RAM ICs with > 1 Bit/Word

> 8x2

![6](6.png)

##### Making Larger Memories: Word extension

![7](7.png)

![8](8.png)

##### Making Wider Memories: Bit extension

![9](9.png)

 ![10](10.png)



#### Dynamic RAM

**information stored as electrical charges**

![11](11.png)

* Read will affect the stored information(has to write again)

![12](12.png)

#### Read & Write

![13](13.png)

![14](14.png)

#### Types

##### Synchronous DRAM (SDRAM)

**Transfers to and from the DRAM are synchronize with a clock**

**Synchronous registers appear on:**

* Address input
* Data input
* Data output

**Column address counter**

* for addressing internal data to be transferred on each clock cycle
* **beginning with the column address counts up to column address + burst size – 1**

**Example: Memory data path width: 1 word = 4 bytes**

![16](16.png)

SDRAM *burst* time-- burst size=4 

![15](15.png)

##### Double Data Rate SDRAM (DDR SDRAM)

* **Transfers data on both edges of the clock**

* **Provides a transfer rate of 2 data words per****clock cycle**

*  **Example: Same as for synchronous DRAM**

  Read cycle time = 60 ns

  Memory Bandwidth: (2 x 32)/(60 x 10-9) = 1.066 Mbytes/sec

* **SRAM as Cache -- read more memory than expected makes CPU reads faster when asking for other data(CPU reads from SRAM)**

  **SPEED UP!**

##### RAMBUS® DRAM (RDRAM)

![17](17.png)

![18](18.png)

### Dependence on Power Supply 

#### Volatile

**Loses stored information when power turned off**

#### Non-volatile

**Retains information when power turned off**
