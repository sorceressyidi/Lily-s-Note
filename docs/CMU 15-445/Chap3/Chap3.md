<font face = "Times New Roman">

## Database Storage
![2](2.png)
![1](1.png)

* Volatile : Not persistent when loose power.
  Random Access Byte Addressable Memory.
* Non-Volatile : Persistent when loose power.
  Sequential Access Block Addressable Memory.
> In the course, we will focus on the DRAM

* Goal : Allow the DBMS to manage databases that exceed 
the amount of memory available
* Reading/writing to disk is expensive, so it must be managed carefully to avoid large stalls and performance degradation.
* Random access on disk is usually much slower than sequential access, so the DBMS will want to maximize sequential access.
![3](3.png)
> Virtual Memory : A technique that allows an operating system to provide more memory to a process than is physically available.
#### Why not use OS?
![4](4.png)

* At this point, no more free memory is available, so the **OS** must swap some memory to disk to make room for the new memory. 
* When we start writing to disk, problematic.
* **OS** is not aware of the DBMS's needs, so it may swap out pages that are important to the DBMS!
![5](5.png)
## How the DBMS represents the database in files on disk?
* Commonly, we store different parts of the database in different files. 
* But also multitable clustering file organization.
![10](10.png)

* Self-contained file : A file that contains all the information needed to manage the data it contains.
> While not entirely true, as the DBMS may store some information to manage the data in other files.
### File Storage
* Different DBMSs manage pages in files on disk in different ways.
![6](6.png)

* like for SQLite,Only 4KB is atomatic read/write!--Hardware can only guarantee atomicity at 4KB.
#### Heap File Organization
* A heap file is an unordered collection of pages with tuples that are stored in random order
> If store tuples one by one , do not guarantee that the tuples are stored in that order.

##### Naive Approach : Linked List.
![7](7.png) 

* If you want to read a tuple, you must search through the entire file to find it.
* While if stored sequentially, search maybe easy, but the tradeoff is when insertion:we have to cannot insert at a random free space, but have to insert at the right place.
![8](8.png)
##### Improved Approach : Page Directory.
![9](9.png)

* Hash Table.[Page Size : Different DBMSs use different page sizes, but 4KB is common.]
#### Tree File Organization
* B+ Tree (See later chapters)
#### Sequential/Sorted File Organization
As demonstrated in `Heap File Organization`, the tradeoff between read and write is a common problem in database storage.
#### Hashing File Organization
* See later chapters.
### Page Layout
Every page contains a header of metadata about the page's contents.
→ Page Size
→ Checksum
→ DBMS Version
→ Transaction Visibility
→ Compression Information
* Some systems require pages to be self-contained (e.g., Oracle)
#### Tuple-oriented Layout
![11](11.png)

* We cannot just fit another tuple in the space left by the deleted tuple, as the tuples are of different sizes!
**Slotted Pages**
![12](12.png)

??? "Details"

    <div align=center> ![13](13.png) </div>  

* How to track Tuples ?
![14](14.png)
#### Log-structured Layout
![18](18.png)
When the page gets full, the DBMS writes it out disk and starts filling up the next page with records.

* → All disk writes are sequential.
* → On-disk pages are immutable.
While difficult to read tuples.
??? "Details"

    <div align=center> ![19](19.png)![20](20.png) </div>  
##### Log-Structured Compaction
Compaction coalesces larger log files into smaller files by removing unnecessary records.
![21](21.png)
Log-structured storage managers are more common today. This is partly due to the proliferation of RocksDB.
Downsides:
* Write - Amplification
* Compaction is expensive
### Tuple Layout
![15](15.png)
#### Denormalized Tuple Data
??? "Details"

    <div align=center> ![16](16.png)![17](17.png) </div>  

### Tuple Storage
#### Data Representation
##### Variable Precision Numbers & Fixed Precision Numbers
> Variable Precision Numbers : Typically faster than arbitrary precision numbers but can have rounding errors...

![22](22.png)
##### Large Values
![23](23.png)
##### External Value Storage
![24](24.png)

### System Catalog
> See Slides.

</font>

