#include <bits/stdc++.h>

using namespace std;

int main() {
    int t; 
    int ang, g, k, n;

    cin >> t;
    for (int i  = 0; i < t; i++) {
        cin >> ang;
        g = __gcd(ang, 180);
        k = ang/g;
        n = 180/g;

        if (k+1 == n)
            k *= 2, n*=2;

        cout << n << endl;
    }

    return 0;
}