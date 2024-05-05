## Copy Ctor
```c++
void f(){
    Stash students();
}
```

* `Stash students();` is a function prototype, while `students` is a function that returns a `Stash` object.

```c++
#include<iostream>
using namespace std;
class A{
    int i;
public:
    A(){cout<<"A()"<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal(){return i;}
    void setVal(int i){this->i=i;}
};
void f(A aa){
    cout << "aa: "<<&aa << endl;
    cout << aa.getVal() << endl;
}
int main(){
    A a;
    a.setVal(10);
    cout << "a: "<<&a << endl;
    cout << "-------------------\n";
    f(a);
    cout << "-------------------\n";

    return 0;
}
```
```
A()
a: 0x16dc9f088
-------------------
aa: 0x16dc9f068
10
~A()
-------------------
~A()
```

* Only one time of constructor is called.
```c++
#include<iostream>
using namespace std;
class A{
    int i;
public:
    A(int i){cout<<i<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal(){return i;}
    void setVal(int i){this->i=i;}
};
void f(A aa){
    cout << "aa: "<<&aa << endl;
    cout << aa.getVal() << endl;
}
int main(){
    A a(10);
    a.setVal(10);
    cout << "a: "<<&a << endl;
    cout << "-------------------\n";
    f(a);
    cout << "-------------------\n";

    return 0;
}
```

* Without default constructor, still one time of constructor is called.
```c++
#include<iostream>
using namespace std;
class A{
    int i;
public:
    A(int i){cout<<i<<endl;}
    A(const A& r):i(r.i){cout<<"A(const A&)"<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal(){return i;}
    void setVal(int i){this->i=i;}
};
void f(A aa){
    cout << "aa: "<<&aa << endl;
    cout << aa.getVal() << endl;
}
int main(){
    A a(10);
    a.setVal(10);
    cout << "a: "<<&a << endl;
    cout << "-------------------\n";
    f(a);
    cout << "-------------------\n";

    return 0;
}
```
```
10
a: 0x16b763088
-------------------
A(const A&)
aa: 0x16b763068
10
~A()
-------------------
~A()
```

* in f(), `A(const A&)` is called.
* `A(const A&)` is a copy constructor.

### When is copy ctor called?
* When an object is constructed.
```c++
Person baby_a("Fred");
// these use the copy ctor
Person baby_b = baby_a; // not an assignment
Person baby_c( baby_a ); // not an assignment
```
* Two implicit cases:
    * When an object is passed by value.[引用或指针不会调用copy ctor]
    * When an object is returned by value.
#### Cases when we want to define our own copy ctor
* When we want to do a partial copy.
* Pointer!!!
> 如果有成员变量是指针，会和原来对象一样指向同一块内存!
> 如果有一个对象被析构，那么这块内存就被 delete, 这就变成了无效内存!

#### Tips
* In general, be explicit
* Create your own copy ctor -- don't rely on the default
* If you don't need one declare a private copy ctor:私有的拷贝构造函数使得对象不能被拷贝构造
  * prevents creation of a default copy constructor
  * generates a compiler error if try to pass-by-value - don't need a defintion

```c++
#include<iostream>
using namespace std;
class A{
    int i;
    string s;
public:
    A(int i){cout<<i<<endl;}
    A(const A& r):i(r.i),s(r.s){cout<<"A(const A&)"<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal(){return i;}
    void setVal(int i){this->i=i;}
};
A f(A aa){
    A bb(20);
    cout << "aa: "<<&aa << endl;
    cout << aa.getVal() << endl;
    return bb;
}
int main(){
    A a(10);
    a.setVal(10);
    cout << "a: "<<&a << endl;
    cout << "-------------------\n";
    A d = f(a);
    cout << "-------------------\n";
    d.setVal(30);
    return 0;
}
```
```
10
a: 0x16dd97070
-------------------
A(const A&)
20
aa: 0x16dd97010
10
~A()
-------------------
~A()
~A()
```

* 编译器在return处优化了，也就是直接把bb放在要返回的地方，而不是在函数内部创建一个临时对象，然后再拷贝到返回的地方

## Overloaded Operators
* Types that cannot be overloaded:
    * `::` `.*` `.` `?:`
    * `sizeof` `typeid`
    * `new` `delete` `new[]` `delete[]
    * `static_cast` `dynamic_cast` `const_cast` `reinterpret_cast`

* Only existing operators can be overloaded.
* Overloaded operators must Preserve number of operands and Preserve precedence
* Operators must be overloaded on a class or enumeration type

### How to overload operators
* keyword `operator` followed by the operator to be overloaded
####  As a member function
```c++
class A {
public:
    A(int ii):i(ii){}
    int get() {return i;}
    /* 返回的一定是 A 的一个新的对象 */
    const A operator+(const A &that) const {
        A c(this->i+that.i);        /* 这里可以访问 that. 私有是针对类的，不是针对对象的。 */
        return c;
    }
private:
    int i;
}
int main() {
    A a = 6;
    A b = 7;
    A c = a + b;    /* a + 9 也是可以的；但 9 + a 不行 */
    cout << c.get() << endl;    /* 输出 13 */
}
``` 

* Why use `const`?
    * `const` member functions can be called on `const` objects
    * `const` objects can only call `const` member functions
    * `const` member functions can't change the object
    * `const` member functions can't call non-const member functions
  * And we don't want to change the object in `operator+`

```c++
#include<iostream>
using namespace std;
class A{
    int i;
public:
    A(int i):i(i){cout<<"A()"<<i<<endl;}
    A(const A& r):i(r.i){cout<<"A(const A&)"<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal(){return i;}
    void setVal(int i){this->i=i;}
    A operator+(const A& r){
        cout << "operator+" << endl;
        A a(this->i+r.i);
        return a;
    }
};
int main(){
    A a(10);
    A b(20);
    A c = a+b;
}
/*
A()10
A()20
operator+
A()30
~A()
~A()
~A()
 */
```

* `A c = a+b;` is equivalent to `A c = a.operator+(b);`
* `A c = a+3;` is equivalent to `A c = a.operator+(3);`
* And when using '3' as the second operand,we construct a temporary object of A(3) and pass it to the operator+ function.
```c++
#include<iostream>
using namespace std;
class A{
    int i;
public:
    A(int i):i(i){cout<<"A()"<<i<<endl;}
    A(const A& r):i(r.i){cout<<"A(const A&)"<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal(){return i;}
    void setVal(int i){this->i=i;}
    A operator+(const A& r){
        cout << "operator+" << endl;
        A a(this->i+r.i);
        return a;
    }
};
int main(){
    A a(10);
    A b(20);
    A c = a+3;
}
/*
A()10
A()20
A()3
operator+
A()13
~A()
~A()
~A()
~A()
*/
```

* However, if we want to use `3+a` , member function can't be used!!!

#### As a global function
* Explicit **First Argument** 
* Developer does not need special access to the classes
* May need to be a `friend` of the class
* Type conversinos performed on **BOTH arguments**
```c++
#include<iostream>
using namespace std;
class A{
    int i;
public:
    A(int i):i(i){cout<<"A()"<<i<<endl;}
    A(const A& r):i(r.i){cout<<"A(const A&)"<<endl;}
    virtual ~A(){cout<<"~A()"<<endl;}
    int getVal()const{return i;}
    void setVal(int i){this->i=i;}
};
A operator+(const A& r,const A&l){
        cout << "+outside" << endl;
        A temp(r.getVal()+l.getVal());
        return temp;
}
int main(){
    A a(10);
    A b(20);
    A c = 3+a;
}
/*
A()10
A()20
A()3
+outside
A()13
~A()
~A()
~A()
~A()
*/
```
#### VS
* Unary operators should be members.
* Assignment operators `=`,`()`,`[]` ,`->` and `->*` must be members.
* All other binary operators as non-members!

**Note : What if A class don't have getVal() function?**
* We can use `friend` to access private members of class A.
```c++
friend const A operator+(const A& r,const A&l); 
```
