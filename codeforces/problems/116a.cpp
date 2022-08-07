#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, p = 0, max_p = 0;
    int in, out;
    cin >> n;
    while (n--) {
        cin >> out >> in;
        p = p - out + in;
        if (p > max_p)
            max_p = p;
    }
    cout << max_p << endl;
}
