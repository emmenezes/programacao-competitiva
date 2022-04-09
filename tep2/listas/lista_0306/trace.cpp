#include <bits/stdc++.h>

using namespace std;

const double PI = acos(-1.0);

int main() {
    int n, signal = 1, ans = 0;
    double ans2;
    int r[100];

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> r[i];

    sort(r, r+n);

    for (int i = n - 1; i >= 0; i--){
        if (signal)
            ans += r[i]*r[i];
        else
            ans -= r[i]*r[i];
        signal = 1 - signal;
    }

    ans2 = PI * ans;
    printf("%.6f\n", ans2);
    
    return 0;
}