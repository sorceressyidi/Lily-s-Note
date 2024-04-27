#include <iostream>
using namespace std;
class A{
  public:
    int i;
    virtual void f(){cout<<"A::f()"<<endl;}
    A(){i=10;cout<<"A()"<<i<<endl;f();}
    void g(){f();}//this->f()
};
class B:public A{
  public:
    int i;
    void f(){cout<<"B::f()"<<endl;}
    B(){i=20;cout<<"B()"<<i<<endl;}
};
int main(){ 
  B b;
  A a;
  A *p=&b;
  cout << sizeof(b)<<endl; //4
  cout << sizeof(A)<<endl; //8
  b.f();
  long long **vp = (long long**)p;
  void (*pf) () = (void (*)())(*(*vp));
  cout << "-------------"<<endl;
  pf();

  p->g();
    cout << "-------------"<<endl;
a = b;
p = &a;
p -> f();

}

