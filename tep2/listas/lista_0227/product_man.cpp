#include <bits/stdc++.h>

using namespace std;

int main() {
    long long int a, b, c, d;
    long long int e, f, g, h;

    cin >> a >> b >> c >> d;
    e = a*c;
    f = a*d;
    g = b*c;
    h = b*d;

    cout << max({e,f,g,h}) << endl;

    return 0;
}