#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m=0,k=0,l;
    size_t p;
    string a;
    while(getline(cin,a)){
        if(a[0] == '+') m++;
        else if(a[0] == '-') m--;
        else {
            k+=m*(a.size()-a.find(':')-1);
        }
    }
    cout << k <<endl;
    return 0 ;
}