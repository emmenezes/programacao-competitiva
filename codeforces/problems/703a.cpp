#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    int m = 0, c = 0;
    int a, b;
    cin >> n;

    while(n--){
        cin >> a >> b;
        if (a > b)
            m++;
        else if (b > a)
            c++;
    }
    if (m > c)
        cout << "Mishka" << endl;
    else if (c > m)
        cout << "Chris" << endl;
    else
        cout << "Friendship is magic!^^" << endl;
}