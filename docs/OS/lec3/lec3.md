<font face = "Times New Roman">

# Lecture 3 - Process

## Process Concept

Process：a unit of resource allocation and protection.

```
Process = code (also called the text)
            initially stored on disk in an executable file
          data section
             global variables (.bssand .data in x86 assembly)
          program counter
            points to the next instruction to execute (i.e., an address in the code)
          contents of the processor's registers
          a stack
          a heap
----------------------------------------------
|                 Stack                      |
|--------------------------------------------|
|                  |                         |
|                  v                         |
|                 ...                        |
|                 ...                        |
|                  ^                         |
|                  |                         |
|--------------------------------------------|
|                 Heap                       |  
|--------------------------------------------|
|                 Data                       |
|--------------------------------------------|
|                 Code                       |
----------------------------------------------
```
![1](0.png)

* Stack pointer & Frame pointer
  * Stack pointer: points to the top of the stack
  * Frame pointer: points to the top of the current function's stack frame


* Why stack is quicker than heap?
  * Much contents in stack are in the cache

### Runtime Stack

* Two processes share the same code, but have different runtime stack/heap.

![2](2.png)

* Dijkstra's stack model

![3](3.png)

## Process Control Block
Each process has and only has a PCB

* Allocate a PCB on new process creation
* Free the PCB on process termination

Represented by the C structure **task_struct**
![4](4.png)

## Process State

![5](5.png)

* process 0 is the idle process
  
  1. Process 0 run when no other process is running
  2. Process 0 -> process 1
* process 1 is the init process
  
  1. Process 1 is the parent of all other processes
* systemd is the init process in modern Linux
  
  1. systemd is the parent of all other processes
  2. systemd is the first process to run after the kernel is loaded
  3. when systemd terminates -- user space ternimated, the system will reboot

### Process Creation

#### The `fork()` System Call

* `fork()` creates a new process
* The child is is a copy of the parent, but...
  
  1. It has a different pid(and thus ppid)
  2. Its resource utilization (so far) is set to 0
  
* `fork()` returns the child’s pid to the parent, and **0** to the child
* Each process can find its own pidwith the `getpid()` call, and its ppidwith the `getppid()` call
* Both processes continue execution after the call to `fork()`

```c
pid=fork();
if (pid<0) {
    fprintf(stdout, "Error: can’t fork()\n");
    perror(“fork()”);
}
if(pid!=0) {
    fprintf(stdout, "I am parent and my child has pid%d\n",pid);while(1);
} else{
    fprintf(stdout, "I am child, and my pidis %d\n", getpid());while(1) ;
}
```

* Further Explian:
  
  1. Child prcess is a copy of the parent process!
  2. Next line for child is also `if(pid!=0)`, but for child, `pid` is 0, so the child will not enter the `if` block

```c
int a = 12
if(pid = fork()){// PARENT
    // ask the OS to put me in waiting
    sleep(10); // 10 seconds
    fprintf(stdout,"a =%d\n",a);
}
else{//CHILD
    a += 3;
    while(1);
}
``` 

* What is the output of the above code?
  
  1. The parent process will print `a = 12`
  2. The child process **cannot** modify the parent's memory space

![6](6.png)

* How many times will the following code print "Hello"?
```c
pid1 = fork();
printf("Hello\n");
pid2 = fork();
printf("Hello\n");
```

* 6 times
  
![7](7.png)
![8](8.png)
![9](9.png)
![10](10.png)
![11](11.png)

#### UNIX examples

* `fork()` system call creates new process
* `execve()` system call used after a `fork()` to **replace the process’memory space with a new program**
* Parent process calls `wait()` for the child to terminate

![12](12.png)

> Demo of how the system do `ls`

![13](13.png)

> 具体来说，当一个进程调用 exec 系列函数（例如 execl()、execv() 等）时，它会用一个新的程序替换当前进程的内容。调用成功后，旧的程序代码、数据和栈都会被新程序的内容取代，但进程ID（PID）保持不变，这意味着新程序继续在同一个进程中运行。此时，当前进程的所有执行状态都会被新程序的状态替代，原进程的代码不会再执行。

#### pros and cons of `fork()`
* Pros
  
  1. 简洁：WindowsCreateProcess需提供10个参数
  2. 分工：fork搭起骨架，exec赋予灵魂
  3. 联系：保持进程与进程之间的关系
* Cons
  
  1. 复杂：两个系统调用
  2. 性能差
  3. 安全性问题

#### DEMO
![14](14.png)

* Originally, highlighted part is in the parent process [in the third `else`],so the parent process will print "Will I be executed?"
* After `fork()`, the child process do `execve()`, so the child process will not print "Will I be executed?"; it will call another program
### Process Termination

![15](15.png)
#### Wait and Waitpid

* A parent can wait for a child to complete 
* The `wait()` syscall 
  1. blocks until **any** child completes
  2. returns the pidof the completed child and the child’s exit code
* The `waitpid()` call
  1. blocks until a **specific** child completes
  2. can be made non-blocking with WNOHANG options
   > Read the man pages (`man 2waitpid`)
### Process and Signal

> Like Ctrl+C -- SIGINT

![16](16.png)

#### Zombie Process
Question: what resources cannot be deallocated by the child process?

* PCB (Process Control Block) is deallocated by the parent process

![18](18.png)

* A process that has terminated, but whose parent has not yet called `wait()`
* The process is in the `Z` state

![17](17.png)

* Add `wait()` to the parent process to avoid zombie process or `waitpid(pid)`

#### Orphan Process
![19](19.png)

* Another way to avoid zombie process:

```c
if(pid<0){
    fprintf(stdout, "Error: can’t fork()\n");
    perror(“fork()”);
}
if(pid!=0){
    fprintf(stdout, "I am parent and my child has pid%d\n",pid);
    while(1);
    //did not call wait() not properly
} else{ //I am the child
      pid = fork();
      if(pid<0){
          fprintf(stdder,"Error: can't fork()\n");
          perror("fork()");
          exit(1);
      }
      if(pid==0){
          fprintf(stdder,"I am the grandchild, and my pid is %d\n",getpid());
          sleep(10);
          exit(0);
      }
      else{
          sleep(1);
          // parent exits without waiting for the child
          // grandchild becomes an orphan -- not a zombie
          exit(0);
      }
}
```
  
## Process Scheduling

* Ready queue : A set of all processes residing in main memory, ready and waiting to execute.
  * Not empty -- IDLE process always in the ready queue
  * Only one ready queue in the system
* Wait queue - A set of processes waiting for **an event**.
* Processes migrate among the various queues.

* 当我们想要插入一个新的进程时，直接通过双向链表接上即可。
  * 通过**偏移量找到对应地址**，并通过强制类型转换得到 **task_struct**。

![20](20.png)

* 当我们想要插入一个新的进程时，直接通过双向链表接上即可。通过偏移量找到对应地址，并通过强制类型转换得到 task_struct。

![21](21.png)

* P and C who will run first?
  * Depends on the Scheduler

### Context Switch
![22](22.png)

* Context switch is the process of saving the state of the current process and restoring the state of a new process.
* CPU only has one register set [Context] => [Register Set]
* Context Switch is **Pure Overhead**
  1. Should be minimized.

* Code

![23](23.png)

1. Save the current process's context 
   1. cpu_context in task_struct, which is a pointer to the current process's context
   2. Save the current process's context to the cpu_context[in task_struct]
   3. Save the current process's stack pointer to the task_struct
2. `x8` points to the task_struct of the process to be switched in
   1. Load the new process's context from the cpu_context[in new task_struct]
   2. Load the new process's stack pointer from the new task_struct

* When is the ret value of `switch_to()` set ?


![24](24.png)


* Now, `task_struct` is on the heap.
* Context Switch is in **Kernel Mode**. 
* Why `fork()` can return two different values in parent and child processes?
  * Because `fork()` , then, two set of context values.

* see https://note.hobbitqia.cc/OS/chap02/#context-switch


### Lab

注：在我们的实验里，`do_timer` trap 切换到**kernel space！**，然后调用 `schedule()` 函数，然后调用 `switch_to()` 函数，最后切换到下一个进程。


</font>