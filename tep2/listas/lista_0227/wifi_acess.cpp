#include <bits/stdc++.h>

using namespace std;

string solve(int n, int routers[100][3], int x, int y){
    int flag = 0, d;
    for (int i = 0; i < n; i++){
        d = (routers[i][0] - x)*(routers[i][0] - x) + (routers[i][1] - y)*(routers[i][1] - y);
        if (d <= routers[i][2]*routers[i][2]){
            flag = 1;
            break;
        }
    }
    if (flag)
        return "Yes";
    else
        return "No";
}

int main() {
    int t;

    cin >> t;

    for (int i = 0; i < t; i++){
        int routers[100][3], accessx, accessy;
        int n, y;

        cin >> n >> y;
        for (int j = 0; j < n; j++){
            cin >> routers[j][0] >> routers[j][1] >> routers[j][2];
        }

        printf("Case %d:\n", i+1);
        for (int j = 0; j < y; j++){
            cin >> accessx >> accessy;
            cout << solve(n, routers, accessx, accessy) << endl;
        }
    }

    return 0;
}