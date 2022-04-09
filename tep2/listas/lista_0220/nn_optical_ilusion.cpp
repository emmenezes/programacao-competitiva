#include <iostream>
#include <cmath>

using namespace std;

const double PI = acos(-1.0);

int main() {
    double n, r, s, R;

    cin >> n >> r;

    s = sin(PI/n);
    R = r*s/(1 - s);

    printf("%.8f", R);

    return 0;
}