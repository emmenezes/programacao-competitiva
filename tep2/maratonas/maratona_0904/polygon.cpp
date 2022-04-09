#include <bits/stdc++.h>

using namespace std;

const double PI = acos(-1.0);

int main() {
    double r, n;
    double ans, ang;

    while (cin >> r >> n){
        ang = 2*PI/n;
        ans = 0.5 * n * r * r * sin(ang) ;
        printf("%0.3lf\n", ans);
        
    }

    return 0;
}