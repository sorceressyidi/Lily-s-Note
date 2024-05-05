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
  cout << "----------"<<endl;
  p->f();
  cout << sizeof(b)<<endl; 
  cout << sizeof(A)<<endl; 
  
  int *pi = (int*)p;
  cout<< long(pi[0]) <<","<<pi[2]<<","<<pi[3]<<endl;

  long long **vp = (long long**)(p);
  void (*pf) () = (void (*)())(*(*vp));
  pf();
  p->g();

  cout << "-------------"<<endl;
  a = b;
  p = &a;

  pi = (int*)p;
  cout<< long(pi[0]) <<","<<pi[2]<<endl;

  long long **vp1 = (long long**)(p);
  void (*pf1) () = (void (*)())(*(*vp1));
  pf1();
  cout<<"-----------"<<endl;
  b.f();
  a.f();
  p -> f();

  cout <<"----------"<<endl;
  A *x1 = new A();
  B *x2 = new B();
  
  x1 = x2;
  cout << "-----------"<<endl;
  x1->f();

}

