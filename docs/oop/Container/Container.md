## Container	

Collection objects are objects that can store an arbitrary number of other objects.

### Vector

#### Example.1

```C++
#include <iostream>
using namespace std;
#include<vector>
int main(){
  vector<int> x;
  for (int a=0;a<1000;a++){
    x.push_back(a);
  }
  vector<int>::iterator p;
  for(p=x.begin();p<x.end();p++)
    	cout << *p << " ";
  return 0; 
}
```

```C++
int main(){
  vector<int> x;
  for(int a=0;a<100;a++){
    x.push_back(a);
  }
  cout << x.size()<<endl
    vector<int>::iterator p;
  for(auto k : x){
    cout << k << " ";
  }
  cout << endl;
  return x;
}
```

* iterator : class inside vector

* generic classes `vector<string> notes;`

  Have to specify two types

![1](1.png)

![2](2.png)

* Insert & erase -- use iterator

#### Example.2

```C++
int main(){
  vector<Student> ss //Student is a class
  Student s(1);
  ss.push_back(s);
  s.x = 10; // does not change ss[0]
}
```

```C++
int main(){
  vector<Student*> ss 
  Student s(1);
  ss.push_back(&s);
  s.x = 10; //will change(obviously)
}
```

#### Operations

* 对于，比如`<vector>` 可以向任意下标赋值，不会报错，但是这不会改变`.size() .back()`等 ，所以实际上我们要用`push_back()`等去insert

### List

![3](3.png)

* Dif : `p!=s.end()`

```C++
#include <iostream>
using namespace std;
#include<list>
list <int> L;
for(int i=0;i<5;i++){
  L.push_back(i)
}
L.erase(++L.begin())
copy(L.begin(),L.end(),ostream_iterator<int>(cout,","));
```

![4](4.png)

> 通常用vector ： 更节约空间,除非需要大量增加，删除

### Maps

> Hash

```C++
#include <map>
map<long,int> root;
root[4] = 2;
root[1000000] = 1000;
long l;
cin >> l;
if (root.count(l))
    cout<<root[l]
else cout<<“Not perfect square”;
```

### Pitfalls

```C++
if ( my_list.count() == 0 ) { ... } // Slow
if ( my_list.empty() ) {...} // Fast
```

* Erase for Iterator !

  ```C++
  list<int> L;
  list<int>::iterator li;
  li = L.begin();
  L.erase(li);
  ++li; // WRONG
  // Use return value of erase to advance
  li = L.erase(li); // RIGHT
  ```

* Inadvertently inserting into `map<>`

  ```C++
  if (foo["bob"]==1)
  //silently created entry “bob”
  //Solutions: Use count() to check for a key without creating a new entry. if ( foo.count("bob") )
  ```

## Function

#### Function Overloading

```C++
void print(char * str, int width); // #1 
void print(double d, int width); // #2 
void print(long l, int width); // #3 
void print(int i, int width); // #4 
void print(char *str); // #5 
print("Pancakes", 15); 
print("Syrup"); 
print(1999.0, 10); 
print(1999, 12); 
print(1999L, 15);
```

* Can go wrong

#### Default arguments

A default argument is a value given in the declaration that the compiler automatically inserts if you donʼt provide a value in the function call.

```C++
int harpo(int n, int m = 4, int j = 5);
int chico(int n, int m = 6, int j); // illegal
//To define a function with an argument list, defaults must be added from right to left.
int groucho(int k = 1, int m = 2, int n = 3);
beeps = harpo(2);
beeps = harpo(1,8);
beeps = harpo(8,7,6);
```

* **Default arguments** Cannot write in the **def part**,  but the **函数声明！** part.

  ```C++
  void f(int i, int j = 10);
  int main()
  { ...
  }
  void f(int i, int j){
      ...
  }
  // USE IN THIS WAY
  ```

#### Friend [Access Control]

```C++
struct X{
  private:
  	int x;
  public :
  	void initialize();
  	friend void g(X*,int);
  	friend void Y::f(X*);
  	friend struct Z;
  	friend void h();
};
```

### Overhead for a function call

#### Inline Functions

* An inline function is expanded in place , like a preprocessor macro , so the overhead of the function call is eliminated.
* Def for inline is "Actually 声明"
* 当调用函数时，编译器把函数替换到实际位置
* 整个inline函数放入头文件
* 如果放在cpp里，那么只能local使用

```C++
inline int f(int i) {
    return i*2;
}
main() {
    int a=4;
    int b = f(a);   // become b = a * 2;
}
```

```C++
// .h File!!!
class Point{
  ...
  public:
  	inline void print(string & msg = "");
};
inline void Point::print(string & msg = ""){
  ...
}
```

* While 可执行程序size 变大 tradoff for effectiveness
* Better for 宏macro  ：check
* Compiler will automatically do inline or undo inline

```C++

```

#### Tradeoff of inline functions



