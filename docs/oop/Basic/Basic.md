# Basic

## Intro

### In & Out

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

### String

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



