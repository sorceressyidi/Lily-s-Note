<font face = "Times New Roman" >

# Lecture 2 - OS Structure

## System Calls

* An interface which kernel provides to the user space to interact with the kernel to do **privileged operations**
* Syscall : proviledged instruction 

![3](3.png)

### Syscall Number

* Each syscall has a unique number
* Syscall Number is the **INDEX** in the syscall table
* In Different OS, the syscall number is different


### Example Ilustration -- Write()
![0](0.png)
![1](1.png)
![2](2.png)

* First `printf()` function is called, then `write()` function is called. In the `write()` function, there is a **system call** to the kernel. [with syscall number `$0x1`]
* Then, go into **kernel space**, and the kernel will do the actual writing to the file descriptor.

  1) `kernel_entry code` will be called -- Saved all user space registers
  
  2) calls `write syscall handler` -- Get from syscall_table, which is an array
   
```C
SYSCALL_DEFINE3(write, unsigned int, fd, const char __user *, buf, size_t, count)
{
    return ksys_write(fd, buf, count);
}
```

* After write finish, call `ret_to_user` 
  * Restore all saved user space registers
  * Transfer control flow to user space

### System Call Implementation
`System-call interface` maintains a table indexed according to numbers assigned to each system call. Each entry in the table points to the entry point of the system call.

* The system call interface invokes the intended system call in OS kernel and returns status of the system call and any return values
* The caller needs to know nothing about how the system call is implemented

![4](4.png)

### Example : Copy a file

![5](5.png)

* Use `strace` to trace system calls
  * `strace cp file1 file2`
  * `strace -c cp file1 file2` -- Count the number of system calls

```shell
strace cp main.c main.copy 2>&1 |wc -l #175 lines
```

* `2>&1` -- Redirect stderr to stdout
* `|wc -l` -- Count the number of lines

![7](7.png)
![6](6.png)

### Time spent in system calls
* `time ap start_kernel` -- Time spent in system calls

![8](8.png)

* `time` count multiple pid and sum them up, so it seems that the time spent in system calls is more than the actual time spent in the system calls.

* `time grep -Rn start_kernel`

![9](9.png)

### System Call Parameter Passing

![10](10.png)

Three general methods used to pass parameters to the OS

* Simplest: pass the parameters in registers
  * In some cases, may be more parameters than registers
* Parameters stored in a block, or table, in memory, and address of block passed as a parameter in a register 
  * This approach taken by **Linux and Solaris**
* Parameters placed, or pushed, onto the stack by the program and popped off the stack by the operating system
* Block and stack methods do not limit the number or length of parameters being passed

## System Service

![11](11.png)

## Linkers and Loaders

* Linkers are for static linking
* Loaders are for dynamic linking

![12](12.png)
![13](13.png)

* Where does static variable goes? -- `.data` section
* Where does static constant goes? -- `.rodata` section
* Why unintialized in `.bss` instead of `.data`? -- To save space, as `.bss` is not stored in the file
  ![15](15.png)

* `readelf -h main`
  * Entry Address
  * Magic Number : `0x7f 0x45 0x4c 0x46` -- ELF : Linux defines the format of the file using magic number

![14](14.png)

### Linking

#### Static Linking 

* All needed code is packed in single binary, leading to large binary
* 可以移植性强

![16](16.png)

#### Dynamic linking

* Reuse libraries to reduce ELF file size.
* How to resolve library calls?

```shell
readelf -p .interp main
```

* This dump the `.interp` section of the ELF file, which contains the path of the dynamic linker
* It is the loader who resolves lib calls.
  * lib call: like `printf()`
  * loader: `ld-linux-aarch64.so.1`
  
![17](17.png)

#### Running a Binary
![18](18.png)

1. `text` section is r-xp, so it is readable and executable, but not writable
2. `rodata` section is r--p, so it is readable, but not writable or executable
3. `data` section is rw-p, so it is readable and writable, but not executable
4. `.bss`: uninitialized variables. 
> 给一个全局变量不给值，早期编译器记录它在 
> .bss 段里，但没有实际空间，映射到内存时就初始化为 0

5. `stack` and `heap` are rw-p, so they are readable and writable, but not executable -- Anonmous Mapping


![19](19.png)

* While for static linking, the mapping is much less.

![20](20.png)

> 上面的Layout 在用户空间，而不是内核空间

* Memory layout is in user space ?
  * User space: stack, heap, data, text 
  * Kernel space: kernel code, kernel data, kernel stack

#### Questions
* Who setups ELF file mapping? -- kernel: `execve()` system call

![23](23.png)

* Who setups stack and heap? -- `execve()` system call
* Who setups libraries? -- loader

![24](24.png)

![21](21.png)
![22](22.png)

* Dynamic linking has to do more system calls

### Setup a Binary

#### Static Binary

* In `readelf` we see that entry of the `main.static` is `0x400640`
* We find that `0x400640` is the address of the `start` function in the `main.static` binary
* `objdump-d a.out`

![25](25.png)

![26](26.png)

* `regs->pc = pc` here `pc` is the address of the `start` function -- `elf_entry`

![27](27.png)

#### Dynamic Binary

![28](28.png)
![29](29.png)
![30](31.png)

* For dynamic binary, the elf_entry -- `interp_elf_ex -> e_entry` 
* `ld.so` -- Loader **resolves** the library calls
* So loader has to be called first, then the `start` function

![30](30.png)

## Why Applications are Operating System Specific
System calls are different -- name / number

Apps can be **multi-operating system**

* Written in interpreted language like Python, Ruby, and interpreter available on multiple operating systems
* App written in language that includes a VM containing the running app (like Java)
* Use standard language (like C), compile separately on each operating system to run on each

**Application Binary Interface (ABI)** is architecture equivalent of API, defines how different components of binary code can interface for a given operating system on a given architecture, CPU, etc 

## Operating-System Design and Implementation

![31](32.png)

## Operating System Structure

General-purpose OS is very large program

Various ways to structure ones

* Simple structure –MS-DOS
* Monolithic –Unix, Linux
* Layered –an abstraction
* Microkernel –Mach

* [Good Helper Website](https://makelinux.github.io/kernel/map/)

</font>