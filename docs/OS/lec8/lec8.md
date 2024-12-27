<font face = "Times New Roman">

# Lecture 8 - Synchronization Real World Problems

## Bounded-buffer problem

**Producer** and **Consumer** share n buffers

* the producer generates data, puts it into the buffer
* the consumer consumes data by removing it from the buffer

The problem is to make sure:

* the producer won’t try to add data into the buffer if it is full
* the consumer won’t try to remove data from an empty buffer

> **Solution**: 

* n buffers, each can hold one item
* semaphore mutex initialized to the value 1
* semaphore full-slots initialized to the value 0
* semaphore empty-slots initialized to the value N


### The Producer

```cpp
do {
    //produce an item
    …
    wait(empty-slots);
    wait(mutex);
    //add the item to the buffer
    …
    signal(mutex);
    signal(full-slots);
    } while (TRUE)
```
1. Here two waits cannot be exchanged

* 不然带锁sleep!!

### The Consumer

```cpp
do {
    wait(full-slots);
    wait(mutex);
    //remove an item from buffer
    …
    signal(mutex);
    signal(empty-slots);
    //consume the item
    …
} while (TRUE);
```

## Readers-writers problem

A data set is shared among a number of concurrent processes

* readers: only read the data set; they do not perform any updates
* writers: can both read and write

**The readers-writers problem:**

* allow multiple readers to read at the same time (shared access)
* only one single writer can access the shared data (exclusive access)

### Solution:

* semaphore mutex initialized to 1
* semaphore write initialized to 1
* integer readcount initialized to 0

> This solution is **Reader First**

### The Writer

```cpp
do {
    wait(write);
    //writing is performed
    ...
    signal(write);
} while (TRUE);
```

### The Reader

```cpp

do {
    wait(mutex);
    readcount++;
    if (readcount == 1) wait(write);
    signal(mutex);
    //reading is performed
    ...
    wait(mutex);
    readcount--;
    if (readcount == 0) signal(write);
    signal(mutex);
} while (TRUE);
```

1. `if (readcount == 1) wait(write);` : 第一个reader，把写屏蔽在外
2. `if (readcount == 0) signal(write);` : 最后一个读完，放锁

### Scenery 1

* First comes a reader A -- sleep on `write`
* Then comes a reader B -- sleep on `mutex`
* Then comes a reader C -- sleep on `mutex`
* Then comes a writer -- xxx signal `write`
* A then B C can read

### Scenery 2

* A reader A is reading data and interrupted
* Next to schedule is a writer ?

> 1. writer is **at write's waiting queue**, not at **ready queue**

> 2. So writer cannot be scheduled


### Readers-Writers Problem Variations

#### Reader first

* no reader kept waiting unless writer is updating data
* If reader holds data, new reader just moves on and reads
* **writer may starve**

#### Writer first

* once writer is ready, it performs write ASAP
* If reader holds data, **new reader will wait for suspended writer**
* **reader may starve**

> Solution

* int readcount writecount = 0
* semaphore rmutex initialized to 1
* semaphore wmutex initialized to 1
* semaphore reaTry initialized to 1
* semaphore resource initialized to 1

##### Reader

```cpp
reader() {
<ENTRY Section>
  readTry.P();                 //Indicate a reader is trying to enter
  rmutex.P();                  //lock entry section to avoid race condition with other readers
  readcount++;                 //report yourself as a reader
  if (readcount == 1)          //checks if you are first reader
    resource.P();              //if you are first reader, lock  the resource
  rmutex.V();                  //release entry section for other readers
  readTry.V();                 //indicate you are done trying to access the resource

<CRITICAL Section>
//reading is performed

<EXIT Section>
  rmutex.P();                  //reserve exit section - avoids race condition with readers
  readcount--;                 //indicate you're leaving
  if (readcount == 0)          //checks if you are last reader leaving
    resource.V();              //if last, you must release the locked resource
  rmutex.V();                  //release exit section for other readers
}
```

##### Writer 

```cpp
//WRITER
writer() {
<ENTRY Section>
  wmutex.P();                  //reserve entry section for writers - avoids race conditions
  writecount++;                //report yourself as a writer entering
  if (writecount == 1)         //checks if you're first writer
    readTry.P();               //if you're first, then you must lock the readers out. Prevent them from trying to enter CS
  wmutex.V();                  //release entry section
  resource.P();                //reserve the resource for yourself - prevents other writers from simultaneously editing the shared resource
<CRITICAL Section>
  //writing is performed
  resource.V();                //release file

<EXIT Section>
  wmutex.P();                  //reserve exit section
  writecount--;                //indicate you're leaving
  if (writecount == 0)         //checks if you're the last writer
    readTry.V();               //if you're last writer, you must unlock the readers. Allows them to try enter CS for reading
  wmutex.V();                  //release exit section
}
```

## Dining-philosophers problem

Philosophers spend their lives thinking and eating

* they sit in a round table, but don’t interact with each other
* They occasionally try to pick up 2 chopsticks (one at a time) to eat
* one chopstick between each adjacent two philosophers
*  need both chopsticks to eat, then release both when done
*  Dining-philosopher problem represents multi-resource synchronization

### Solution (assuming 5 philosophers):

> See Slides. [10-29第7-8节]



</font>