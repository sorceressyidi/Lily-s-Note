<font face = 'Times New Roman'>

## In & Out

```C++
#include<iostream>
using namespace std;
int main()
{
  	int age;
    cin >> age >> name;
    return 0;
}
```

* `cout` 标准输出   `<<` Inserter

* `cout` 为 `cout << "Hello World"` 的结果

## String

`#include<string>`

```C++
#include<iostream>
#include<string>
using namespace std;
int main()
{
  	int age;
    string name;
    cin >> age >> name;
    cout << "Hello World!" << name << " is " << age << " today!" << endl;
    cout << name.length() << endl;
    return 0;
}
```

* 字符串结尾非`\0`

`string place("Hangzhou").`

`int a(8)`

#### Sub-string

```C
#include <iostream>
#include <string>
using namespace std;
int main() {
    string originalString = "Hello, World!";
    // Using substr to extract a substring
    int startPos = 7; // Starting position
    int length = 5;   // Length of the substring to extract
    string extractedSubstring = originalString.substr(startPos, length);
    // Displaying the result
    cout << "Original String: " << originalString << endl;
    cout << "Substring from position " << startPos << " with length " << length << ": " << extractedSubstring << endl;
    return 0;
}
```

#### Alter-string

* Assign

```C++
#include <iostream>
#include <string>
using namespace std;
int main() {
    // Original string
    string myString = "Hello, World!";

    // Example 1: Assign the value of another string
    string anotherString = "Goodbye";
    myString.assign(anotherString);
    cout << "After assign(const string& str): " << myString << endl;

    // Example 2: Assign a substring of another string
    string sourceString = "123456789";
    myString.assign(sourceString, 2, 5);  //Starting from position 2,take 5 characters
    cout << "After assign(const string& str, size_t subpos, size_t sublen): " << myString << endl;

    // Example 3: Assign the value of a C-string
    const char* cString = "C-Style String";
    myString.assign(cString);
    cout << "After assign(const char* s): " << myString << endl;

    // Example 4: Assign the first n characters of a C-string
    const char* cStringWithLength = "ABCDE";
    size_t n = 3;
    myString.assign(cStringWithLength, n);
    cout << "After assign(const char* s, size_t n): " << myString << endl;

    // Example 5: Assign a string consisting of n copies of character c
    char characterToRepeat = 'X';
    size_t numberOfCopies = 4;
    myString.assign(numberOfCopies, characterToRepeat);
    cout << "After assign(size_t n, char c): " << myString << endl;

    return 0;
}

```

```
After assign(const string& str): Goodbye
After assign(const string& str, size_t subpos, size_t sublen): 34567
After assign(const char* s): C-Style String
After assign(const char* s, size_t n): ABC
After assign(size_t n, char c): XXXX
```

> `size_t` is a data type in C++ that is commonly employed for expressing the size of objects or the count of elements. It belongs to the category of unsigned integer types and is designed to have a size large enough to handle the maximum possible size of objects on a given platform. The definition of `size_t` can be found in the standard library header `<cstddef>` (or `<stddef.h>` in C), and it is typically introduced using `typedef` or `using`.

* Insert

```C++
#include <iostream>
#include <string>

using namespace std;

int main() {
    // Original string
    string myString = "Hello, World!";

    // Example 1: Insert another string at a specific position
    string insertString = "Beautiful ";
    size_t insertPosition = 7;  // Before the 'W'
    myString.insert(insertPosition, insertString);
    cout << "After insert(size_t pos, const string& str): " << myString << endl;

    // Example 2: Insert a substring of another string at a specific position
    string sourceString = "12345";
    size_t subpos = 2;
    size_t sublen = 3;
    myString.insert(12, sourceString, subpos, sublen);  // Insert at position 12
    cout << "After insert(size_t pos, const string& str, size_t subpos, size_t sublen): " << myString << endl;

    // Example 3: Insert a C-string at a specific position
    const char* cString = "XYZ";
    myString.insert(6, cString);  // Insert at position 6
    cout << "After insert(size_t pos, const char* s): " << myString << endl;

    // Example 4: Insert the first n characters of a C-string at a specific position
    const char* cStringWithLength = "ABCDE";
    size_t n = 3;
    myString.insert(3, cStringWithLength, n);  // Insert at position 3
    cout << "After insert(size_t pos, const char* s, size_t n): " << myString << endl;

    // Example 5: Insert n copies of character c at a specific position
    char characterToInsert = '!';
    size_t numberOfCopies = 4;
    myString.insert(0, numberOfCopies, characterToInsert);  // Insert at the beginning
    cout << "After insert(size_t pos, size_t n, char c): " << myString << endl;

    return 0;
}
```

```
After insert(size_t pos, const string& str): Hello, Beautiful World!
After insert(size_t pos, const string& str, size_t subpos, size_t sublen): Hello, Beaut345iful World!
After insert(size_t pos, const char* s): Hello,XYZ Beaut345iful World!
After insert(size_t pos, const char* s, size_t n): HelABClo,XYZ Beaut345iful World!
After insert(size_t pos, size_t n, char c): !!!!HelABClo,XYZ Beaut345iful World!
```

* Erase

```C++
#include <iostream>
#include <string>
using namespace std;
int main() {
    // Original string
    string myString = "Hello, World!";
    // Example 1: Erase a portion of the string
    size_t erasePosition = 7;  // Start erasing from position 7
    size_t eraseLength = 5;    // Erase 5 characters
    myString.erase(erasePosition, eraseLength);
    cout << "After erase(size_t pos, size_t len): " << myString << endl;
    // Example 2: Erase the entire string (using default arguments)
    myString.erase();
    cout << "After erase(): " << myString << endl;
    return 0;
}
```

```
After erase(size_t pos, size_t len): Hello, !
After erase(): 
```

* Replace

```C++
#include <iostream>
#include <string>

using namespace std;

int main() {
    // Original string
    string myString = "Hello, World!";

    // Example 1: Replace a portion of the string with another string
    size_t replacePosition = 7;        // Start replacing from position 7
    size_t replaceLength = 5;           // Replace 5 characters
    string replacementString = "Universe";
    myString.replace(replacePosition, replaceLength, replacementString);
    cout << "After replace(size_t pos, size_t len, const string& str): " << myString << endl;

    // Example 2: Replace a portion of the string with a substring of another string
    string sourceString = "12345";
    size_t subpos = 2;
    size_t sublen = 3;
    myString.replace(12, 5, sourceString, subpos, sublen);  // Replace at position 12
    cout << "After replace(size_t pos, size_t len, const string& str, size_t subpos, size_t sublen): " << myString << endl;

    // Example 3: Replace a portion of the string with a C-string
    const char* cString = "XYZ";
    myString.replace(6, 5, cString);  // Replace at position 6
    cout << "After replace(size_t pos, size_t len, const char* s): " << myString << endl;

    // Example 4: Replace a portion of the string with the first n characters of a C-string
    const char* cStringWithLength = "ABCDE";
    size_t n = 3;
    myString.replace(3, 5, cStringWithLength, n);  // Replace at position 3
    cout << "After replace(size_t pos, size_t len, const char* s, size_t n): " << myString << endl;

    // Example 5: Replace a portion of the string with n copies of character c
    char characterToReplace = '!';
    size_t numberOfCopies = 4;
    myString.replace(0, 1, numberOfCopies, characterToReplace);  // Replace at the beginning
    cout << "After replace(size_t pos, size_t len, size_t n, char c): " << myString << endl;

    return 0;
}
```

```
After replace(size_t pos, size_t len, const string& str): Hello, Universe!
After replace(size_t pos, size_t len, const string& str, size_t subpos, size_t sublen): Hello, Unive345
After replace(size_t pos, size_t len, const char* s): Hello,XYZe345
After replace(size_t pos, size_t len, const char* s, size_t n): HelABCZe345
After replace(size_t pos, size_t len, size_t n, char c): !!!!elABCZe345
```

* Find

```C++
#include <iostream>
#include <string>
using namespace std;
int main() {
    // Original string
    string myString = "Hello, World!";
    // Example 1: Find the position of a substring
    string searchString = "World";
    size_t foundPosition = myString.find(searchString);
    cout << "Position of '" << searchString << "': " << foundPosition << endl;
    // Example 2: Find the position of a substring starting from a specific position
    size_t startPosition = 7;
    foundPosition = myString.find(searchString, startPosition);
    cout << "Position of '" << searchString << "' starting from position " << startPosition << ": " << foundPosition << endl;
    return 0;
}
```

```
Position of 'World': 7
Position of 'World' starting from position 7: 7
```

## Dynamic memory allocation

`new` and `delete`

```C++
new int;
new int[10];
new Stash;
delete p;
delete []p; //指针指向的是多个对象
```

```C++
// Allocate an array of integers
int* p = new int[5];
// Use the allocated memory
// Deallocate the memory using delete []
delete [] p;
```

* New -- 申请空间，同时初始化对象

* It is safe to delete a `Null`

*  `malloc`  returns `null` indicating not enough space

  `new` just alert error.

## Class

### Declaring references
* Must be initialized when defined
```C++
char c;
char& r=c;
```

> For local or global variables , the initial value of the bending is required.
>
> In parameters lists and member varaibles , not necessary

```C++
void f(int& x);
f(y);	//initialized when function is called 
```

![1](1.png)

**Restrictions**

* No references to references.
* No pointers to references. (References to pointer is OK)
* No arrays of references.

### Intro

```C++
#include <iostream>
#include <string>
using namespace std;
typedef struct point {
    float x;
    float y;
    /*version1*/
    void print(){
        cout << x << " " << y << endl;
    }
    /*version 2*/
    void move(int dx, int dy);
} Point;
void Point::move(int dx, int dy){
    x += dx;
    y += dy;
}
/*void print(const Point *p)
{
    printf("%d %d\n", p->x, p->y); // const means that the function will not change the value of the variable 
}
void move(Point* p,int dx, int dy)
{
    p->x += dx;
    p->y += dy;
}*/
int main()
{
    Point a;
    a.x = 1;
    a.y = 2;
    a.print();
    a.move(3, 4);
}
```

```C++
// Class
#include <iostream>
#include <string>
using namespace std;
class Point{
  public:
    void init(int x,int y);
    void move(int dx,int dy);
    void print()const;
  private:
    int x;
    int y;
};
void Point::init(int ix,int iy){
  x=ix;
  y=iy;
}
void Point::move(int dx,int dy){
  x+=dx;
  y+=dy;
}
void Point::print()const{
  cout<<"("<<x<<","<<y<<")"<<endl;
}
int main()
{
    Point a;
    a.init(10,20);
    a.print();
}
```

* Take for example, the print function , **How does the function knows what exactly is x and y** ?

  ```C++
  void Point::print()const{
    cout << this << endl
    cout<<"("<<this->x<<","<<this->y<<")"<<endl;
  }
  ```

  `this`  -- `Point* this` --hidden parameter

  Another example

  ```C++
  void Point::init(int x,int y){
    this->x=x;
    this->y=y; 
  }
  ```

### Resolver

```C++
void S::f() {
    ::f(); // Would be recursive otherwise!
    ::a++; // Select the global a
    a--; // The a at class scope
}
```

### Object-Oriented

#### Constructer

* Constructer is to initialize , not to allocate memory.
* Once there is a "constructer" ,you cannot initilize by `Point c = {10,20}`

```c++
#include <iostream>
#include <string>
using namespace std;
class Point{
  public:
  	Point(int deep);  //one argument
    Point(int x,int y); //two arguments
  	Point(){x = 13,y=31;}; // no argument
    void move(int dx,int dy);
    void print()const;
  private:
    int x;
    int y;
};
Point::Point(int ix,int iy){
  x=ix;
  y=iy;
}
Point::Point(int deep){
  x=y=deep;
}
void Point::move(int dx,int dy){
  x+=dx;
  y+=dy;
}
void Point::print()const{
  cout<<"("<<x<<","<<y<<")"<<endl;
}
int main()
{
    Point a(10,20);
  	Point c(10);//Point c = 10
  	Point d;
  	d.print();
    a.print();
}
```

* A default constructer is one that can be called with no arguments
* If no default constructer is coded , the compiler will automatically implement one(in default version)

#### Initialization VS assignment

```C++
Student::Student(string s):name(s){} //initialization before constructor
// Prefered
```
> 这意味着我们在构造函数的初始化列表中对 name 成员变量进行了初始化
> 在构造函数体内，我们没有对 name 进行赋值操作，而是在构造函数的初始化列表中直接将传递给构造函数的参数 s 赋值给了 name,这样的操作是在构造函数体执行之前，即在构造函数被调用时，就对 name 进行了初始化
> 因此，可以说这是“初始化（Initialization）在构造函数（Constructor）之前（Before）”执行的，即“initialization before constructor”


**Assignment**

```cpp
Student::Student(string s) {name=s;}
```

* string must have a default constructor  : (先构造出 string 的对象 name, 再赋值)

```C++
Student::Student(sring s){
  name = s;
} //assignment
// For more constructors
```
```C++
void func() {
    int x;  // 在函数内部声明的变量
    				// 空间在函数执行时分配
}
void func() {
    static int x; // 静态变量
    						  // 空间在程序启动时分配
}
```

```C++
#include <iostream>
#include <string>

class Student {
private:
    std::string name;

public:
    // 默认构造函数，使用成员初始化列表对 name 进行初始化
    Student(std::string s) : name(s) {
        std::cout << "Default constructor called with name: " << name << std::endl;
    }
    // 输出学生姓名的方法
    void display() {
        std::cout << "Student's name: " << name << std::endl;
    }
};
int main() {
    // 创建一个名为 "Alice" 的学生对象，并使用默认构造函数进行初始化
    Student student1("Alice");
    // 调用 display 方法显示学生的姓名
    student1.display();
    return 0;
}
```
* const
```C++
class Point {
private:
    const float x, y;
public:
    Point(float xa = 0.0, float ya = 0.0) : y(ya), x(xa) {}
};
```
* Here, const variables cannot be assigned values, they can only be initialized. The initialization of member const variables can be done using const float x = 1.0;, but in this case, all objects of the class will have the same value. Another place where const variables can be initialized within a class is in the constructor's initialization list.

#### Destructor「析构」

* Destructor is called automatically by the compiler when theobject goes out of scope

* The order of destruction is the reverse of construction.

* Scope is delimited by curly braces`{ }`.

* Upon entering a function, space for all local variables is allocated,but constructors are not invoked until the specific constructor line is executed. 

  Similarly, when entering a `switch case` statement, space for objects is generated but not constructed, which may lead to issues during destruction.

```c++
void f(int i){
  if(i<10){
    goto jump1; //Error: goto bypasses init
  }
  X x1;	//Constructor
  jump1:
  	switch(i){
      case 1:
        X x2;//Constructor
      case 2 : //Error: case bypasses init
        X x3;//Constructor
        break;
    }
}
```

* Memory for $x_1$($x_2$) is allocated , but not initialized , so **destruction** will fail

#### Definitions of a class

- In C++, separated `.h` and `.cpp` files are used to define one class.
- Class declaration and prototypes in that class are in the header file ( `.h` ).
- All the bodies of these functions are in the source file (`.cpp`)

* Standard header file sturcture
  ```C++
  #ifnedf HEADER_FLAG
  #define HEADER_FLAG
  //Type declaration here...
  #endif
  ```
  `#include` is to insert the included file into the `.cpp` file at where the `#include` statement is.
- `#include "xx.h"` : search in the *current directory firstly*, then the directories
  declared somewhere
- `#include <xx.h>` : search in the specified directories
- `#include <xx>` : same as `#include <xx.h>`
### Example
`NumberDisplay.h`
```C++
#ifndef _NUMBER_DISPLAY_HEAD_
#define _NUMBER_DISPLAY_HEAD_
#include<string>
class NumberDisplay{
  private:
    int limit;
    int value;
  public:
  NumberDisplay(int limit);
  int increase();
  std::string toString();
}
#endif
```
`NumberDisplay.cpp`
```C++
#include "NumberDisplay.h"
#include<string>
#include<iostream>

NumberDisplay::NumberDisplay(int limit){
  value = 0;
  this->limit = limit;
}
/**
 * @return 1 for turn over
*/
int NumberDisplay::increase():{
  value++;
  if(value == limit){
    value = 0;
    return 1;
  }
  return 0;
}
std::string NumberDisplay::toString(){
  if(value<10){
    return "0"+value;
  }
  else{
    return ""+value;
  }
}
#ifdef _TEST_ND_
#include<iostream>
using namespace std;
int main(){
  NumberDisplay d(10);
  for(int i=9;i<20;i++){
    d.increase();
    cout << d.tostring()<<endl;  
  }

}
#endif
```
`clock.h`
```C++
#ifndef _CLOCK_HEAD_
#define _CLOCK_HEAD_
#include "NumberDisplay.h"
class Clock{
  private:
    NumberDisplay hour;
    NumberDisplay minute;
  public:
     Clock();
     void dida();
}
```
`clock.cpp`
```C++
#include "clock.h"
#include<iostream>
using namespace std;
Clock::Clock():
  hour(24),minute(60) //initialization list
{

}
void Clock::dida(){
  if(minute.increase()){
    hour.increase
  }
  cout << hour.toString();
  cout << ":";
  cout << minute.toString();
  cout << endl;
}
```
* What if ?  `clock.h`

```C++
#ifndef _CLOCK_HEAD_
#define _CLOCK_HEAD_
//#include"NumberDisplay.h"
class NumberDisplay
class Clock{
  private:
    NumberDisplay *hour;
    NumberDisplay *minute;
  public:
     Clock();
     void dida();
}
```

> Reference

引用和指针是C++中两种不同的概念，它们有着相似的功能，但在语义和使用方式上有一些重要的区别。

### 区别一：语法和声明
- **引用**：使用 `&` 符号来声明，必须在初始化时绑定到一个已存在的变量或对象。一旦初始化，引用将一直指向该变量或对象，并且不能重新绑定到其他对象。
  
- **指针**：使用 `*` 符号来声明，可以在任何时候指向一个对象，也可以指向空值（nullptr）。指针可以在运行时被重新赋值，指向不同的对象或空值。

```cpp
int num = 10;
int& ref = num; // 引用
int* ptr = &num; // 指针
```

### 区别二：空值
- **引用**：引用不能指向空值，必须在初始化时绑定到一个已存在的对象。

- **指针**：指针可以指向空值（nullptr），表示不指向任何对象。

```cpp
int& ref = null; // 错误，引用不能指向空值
int* ptr = nullptr; // 指针指向空值
```

### 区别三：操作符
- **引用**：使用引用时，不需要使用解引用操作符（`*`），直接使用引用本身即可访问目标对象。

- **指针**：需要使用解引用操作符（`*`）来访问指针指向的对象。

```cpp
int num = 10;
int& ref = num; // 引用
int* ptr = &num; // 指针

int value1 = ref; // 直接使用引用
int value2 = *ptr; // 使用指针需要解引用
```

### 区别四：空间占用
- **引用**：在内存中不会分配额外的空间，它只是原变量的别名。

- **指针**：在内存中占用额外的空间来存储指针变量本身的地址。

### 总结
引用和指针在C++中都有其独特的用途和优势。引用更安全、更直观，适用于简单的别名和传递参数。指针更灵活，可以指向多个对象，可以进行空值检查，适用于需要动态分配内存或跟踪对象地址的情况。选择使用引用还是指针取决于具体的需求和设计考虑。

</font>