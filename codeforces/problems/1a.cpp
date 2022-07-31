#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, a, ma, na, t, mr, nr;
    
    cin >> n, m, a;

    ma = m / a;
    na = n / a;
    t = ma * na;

    mr = m - ma*a;
    nr = n - na*a;

    if (nr != 0) {
        t += m/a;
        if (m%a != 0) t += 1;
    }
    if (mr != 0) t += n/a;

    cout << t << endl;
    
}