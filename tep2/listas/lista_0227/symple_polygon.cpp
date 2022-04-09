#include <bits/stdc++.h>

using namespace std;

const double PI = acos(-1.0);

int main() {
    int t, n;
    double ans, ang;

    cin >> t;

    for (int i = 0; i < t; i++){
        cin >> n;
        ang = PI/(2*n);
        ans = 1/tan(ang);
        printf("%.6f\n", ans);
    }

    return 0;
}