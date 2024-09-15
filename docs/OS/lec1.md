<font face = "Times New Roman" size = 4>

# Lecture 1 - Introduction to Operating Systems
## 1.0 A bit of history
* Father of Linux - Linus Torvalds (at age 21)
* LLVM - Low Level Virtual Machine by Chris Lattner
* Ubuntu - Linux Core Plus GNU
* Unix - Multitasking, multi-user OS
## 1.1 What is an Operating System?
An operating system is a software that acts as an intermediary between the computer hardware and the user. It provides an environment in which a user can execute programs conveniently and efficiently.
* Resource Manager and Allocator

### Starting an OS
* The first program that runs when a computer starts up is the bootloader -- the  bootstrap program initializes the computer.
* Locates and loads the OS kernel into memory
* Wait for 'event' to occur

### Multi-programming
#### Time-sharing
* Multi-programming with **rapid context switching** -- Actually not working all the same time.
* jobs are called processes

### The running OS
* The kernel is not a running job -- It's code that resides in memory and is ready to be executed at any moment
* OS be executed on behalf of a job whenever requested
* OS do special/dangerous things that user programs can't do
* When designing a kernel : Lean and Mean
  * Lean - Only the necessary features
  * Mean - single minded, focused on the job
* Size of Linux Kernel when loaded in memory is about x MBs to xx MBs
* No memory protection with the kernel
  * The kernel's the one saying to a process "segmentation fault"
  * Nobody's watching over the kernel
  
### Designing an OS
* Design CPU to support OS
* User / Kernel mode -- add a 'mode bit'
  * User mode - restricted mode
  * Kernel mode - unrestricted mode

```
------------------------------------
| APP --> Unprivileged instructions |
------------------------------------
| OS --> Privileged instructions    |
------------------------------------
|  Hardware                         |
------------------------------------
```

### OS Events
An event stops execution, changes mode, and changes context
* System Call - Request to the OS

### System Calls
When a user program need sto do something privileged, it makes a system call
* A special kind of **trap**
* Every ISA provides a system call instruction that 
  * Causes a trap,which maps to a kernel handler
  * Passes a
</font>