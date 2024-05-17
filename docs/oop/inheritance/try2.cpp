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