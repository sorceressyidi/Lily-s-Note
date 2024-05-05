#include <iostream>
using namespace std;
class A {
    public:
        A() { f(); }
        virtual void f() { cout << "A::f()"; }
};
class B : public A {
    public:
        B() { f(); }
        void f() { cout << "B::f()"; }
};
int main() {
    B b;
}