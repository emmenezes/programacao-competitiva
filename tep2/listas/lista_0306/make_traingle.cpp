#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b, c, ans = 0;

    cin >> a >> b >> c;

    while ((a >= b + c) || (b >= a + c) || (c >= a + b)){
        if (a <= b && a <= c)
            a++;
        else if (b < a && b <= c)
            b++;
        else
            c++;
        ans++;
    }

    cout << ans << endl;

    return 0;
}