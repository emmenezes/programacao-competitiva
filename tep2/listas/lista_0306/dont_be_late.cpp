#include <bits/stdc++.h>

using namespace std;

int main() {
    int d, t, s;

    cin >> d >> t >> s;

    if (t*s < d)
        cout << "No" << endl;
    else
        cout << "Yes" << endl;

    return 0;
}