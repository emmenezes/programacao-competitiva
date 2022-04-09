#include <bits/stdc++.h>

using namespace std;

int solve (int n, int r, int a[][2]) {
    int dist_max = 0, dist_temp = 0;
    for (int i = 0; i < n; i++) {
        bool possivel = true;
        for (int j = 0; j < n; j ++) {
            dist_temp = abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1]);
            if (dist_temp > r) {
                possivel = false;
                break;
            }
        }
        if (possivel)
            return 1;
    }
    return -1;
}

int main() {
    int t;
    cin >> t;

    for(int i = 0; i < t; i++) {
        int n, r;
        int x [100] [2]= {{0,0}};

        cin >> n >> r;
        for (int j = 0; j < n; j++) {
            cin >> x[j][0] >> x[j][1];
        }

        cout << solve(n, r, x) << endl;
    }

    return 0;
}