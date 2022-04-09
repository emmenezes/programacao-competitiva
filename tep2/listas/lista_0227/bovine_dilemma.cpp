#include <bits/stdc++.h>

using namespace std;

int solve(int n, int * x) {
    int a[50] = {0};
    int sum = 0;

    for (int i = 0; i < n-1; i++)
        for (int j = i+1; j < n; j ++)
            a[x[j]-x[i]] = 1;

    for (int i = 0; i < 50; i++)
        if (a[i])
            sum ++;

    return sum;
}

int main() {
    int t;
    cin >> t;

    for(int i = 0; i < t; i++) {
        int n;
        int x[50] = {0};

        cin >> n;
        for (int j = 0; j < n; j++) {
            cin >> x[j];
        }

        cout << solve(n, x) << endl;
    }

    return 0;
}