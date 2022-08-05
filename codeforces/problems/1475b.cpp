#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n, r, d;
    cin >> t;
    while (t--) {
        cin >> n;
        r = n%2020;
        d = n/2020;
        if (d >= r) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}