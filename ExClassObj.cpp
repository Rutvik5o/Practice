#include<iostream>
using namespace std;

class demo
{
     private:
     int a,b;

     public:
     void input()
     {
        cout<<"Enter the value of A and B\n";
        cin>>a>>b;
     }

     void show()
     {
        cout<<a<<" "<<b;
     }

};

int main()
{
       demo a;
       a.input();
       a.show();
       return 0;

}