#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    string s;
    
    cin >> n;
    cin >> s;

    auto t0 = count(s.begin(), s.end(), '1');
    auto t1 = count(s.begin(), s.end(), '0');
    
    cout << n - 2*min(t0,t1) << endl;
}