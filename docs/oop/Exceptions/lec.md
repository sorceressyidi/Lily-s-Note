<font face = "Times New Roman" >

## Exceptions
Exceptions are a mechanism for handling errors in C++ programs. They are used to signal that an error has occurred and to specify what should be done to handle the error.

* The significant benefit of exceptions is that they clean up error handling code.

* It separates the code that describes what you want to do from the code that is executed.

可以预见的错误：

* 找不到文件
* 文件虽然存在但是打不开（没有权限、被别的进程打开）
* 文件大小判断失败（可能是一个串口，不是磁盘上的文件，串口是没有结束的）

>可以 fseek 到文件末尾，再 ftell 末尾的值。


```c++
errorCodeType readFile { initialize errorCode = 0;
    open the file;
    if ( theFilesOpen ) { 
        determine its size;
        if ( gotTheFileLength ) { 
            allocate that much memory;
            if ( gotEnoughMemory ) { 
                read the file into memory;
                if ( readFailed ) { 
                    errorCode = -1;
                }
             }else {
                errorCode = -2;
                } 
        } else {
            errorCode = -3;
        }
        close the file;
        if ( theFILEDidntClose && errorCode == 0 ) { 
            errorCode = -4;
    }else {
        errorCode = errorCode and -4;
        } 
    } else {
        errorCode = -5;
    }
    return errorCode;
}
```
* 代码中的错误码是什么意思？--可读性差
```c++
try {
    open the file;
    determine its size;
    allocate that much memory;
    read the file into memory;
    close the file; 
} 
catch ( fileOpenFailed ) { doSomething; } 
catch ( sizeDeterminationFailed ) { doSomething; } 
catch ( memoryAllocationFailed ) { doSomething; } 
catch ( readFailed ) { doSomething; } 
catch ( fileCloseFailed ) { doSomething; }
```
### Example
```c++
template <class T> class Vector { 
private: 
    T* m_elements; 
    int m_size; 
public: 
    Vector (int size = 0) : 
    m_size(size) ... 
    ~Vector () { delete [] m_elements; } 
    void length(int); 
    int length() { return m_size; } 
    T& operator[](int); 
};
```
* 问题：当用户试图访问一个不存在的元素时，应该怎么处理？
```c++
T& Vector::operator[](int index) { 
    if (index < 0 || index >= m_size){
        throw "Index out of range"; 
    }
    return m_elements[index]; 
}
```
* Assertion vs. Exception
  * Assertion is used to check for bugs in the program.
  * Exception is used to check for errors in the program.
* 抛异常之后，后续的代码都不会执行（没遇到的 try{} 的大括号都可以看作异常），然后往外走。
* 上面这里 throw 之后，如果大括号是语句就离开语句，如果是函数就离开函数，如果是 try{}, 我们就判断匹配一个异常类
```c++
class VectorIndexError { 
    public: 
    VectorIndexError(int v) : m_badValue(v) { } 
    ~VectorIndexError() { } 
    void diagnostic() { cerr << "index " << m_ badValue << "out of range!"; } 
    private: 
    int m_badValue; 
    };
    template <class T> T& Vector::operator[](int index) { 
        if (index < 0 || index >= m_size) 
            throw VectorIndexError(index); 
        return m_elements[index]; 
}
```
```c++

void outer2() { 
String err("exception caught"); 
try {
    func(); 
} catch (VectorIndexError) { 
    cout << err; 
    throw; // propagate the exception 
} 
}
```
* try 后面可以跟任意数量的 catch.
>Two forms
catch (SomeType v) { // handler code }
catch (...) { // handler code }

* throw 可以抛的任意类型, int/double/... 也是可以的。一般不会抛原始数据类型，因为表达的信息有限。通常会做一个类，抛类的对象。
* Handlers are checked in order of appearance
按顺序匹配，先匹配前面的，匹配成功后不会寻求下一个匹配。
* Check for exact match
  Apply base class conversions Reference and pointer types, only
* 对象会进行基类转换。一般把子类放在前面。
* Ellipses (...) match all
* `new` does NOT returned 0 on failure. new raises a bad_alloc() exception.

### `void abc():throw (MathErr);`
* 如果有这个声明，那么这个函数里面就不能抛出其他异常，只能抛出 MathErr 异常。抛出了其他异常，编译器会报错，终止程序。
```c++
Printer::print(Document&) : throw(PrinterOffLine, BadDocument) { ... }
PrintManager::print(Document&) : throw (BadDocument) { ... }// raises or doesn’t handle BadDocument 
void goodguy() : throw () { }// handles all exceptions 
void average() { } // no spec, no checking,
```
* 1.表示会抛 PrinterOffLine, BadDocument 异常。（不一定抛，但可能）
* 3.表示不会抛任何异常，这样调用的时候不需要 try catch.
* 4.可能会抛异常，但是编译器不会进行检查。

#### Note:
* 1. in C++ , exception is not a routine and not for good design.
* 2. Exception in constructor : 先分配内存，再执行构造
```c++
f() {
    A *p = new A();
    ...
    delete p;
}
```
* 如果构造的时候出异常, p 无法得到分配的地址，但是内存却没有被析构。内存泄漏！
* Solve:
  1. Never New？
  2. Catch error and `delete this`:必须是一个局部对象，不能是一个全局对象。
    * 如果是 new error类,需要记得同时delete error类.
   ```c++
   Error *p = new Error();
   ...
   catch (Error e) {
       delete e;
       delete this;
    }
    ```
    * 如果是全局的error类，等堆栈清空的时候，会自动析构。
  3. Altimate: 两阶段构造:构造函数不做任何事情(打开网络，读取文件等)，只是分配内存，然后用explicit的init函数（第二阶段构：需要主动调用）来初始化
   * 也就是说构造函数不允许抛异常，只有init函数可以抛异常。

## Complement : stream
```c++
int get()
while((ch=cin.get())!=EOF) {
    cout.put(ch);
}
```

</font>