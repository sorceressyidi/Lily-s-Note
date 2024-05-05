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
    A operator+(const A& r){
        cout << "operator+" << endl;
        A a(this->i+r.i);
        return a;
    }
};
A operator+(const A& r,const A&l){
        cout << "+outside" << endl;
        A temp(r.getVal()+l.getVal());
        return temp;
}
int main(){
    A a(10);
    A b(20);
    A c =a+b;
}
/*
似乎这样也不会出错了
*/