#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n, ans;

    cin >> t;
    while(t--) {
        ans = 1;
        cin >> n;
        int an[n] = {};
        set<int> as;
        for (int i = 0; i <n; i++)
            cin >> an[i];
        for (int i = n-1; i >= 0; i--) {
            auto it = as.find(an[i]);
            if (it == as.end()){
                as.insert(an[i]);
            } else {
                cout << i + 1 << endl;
                ans = 0;
                break;
            }
        }
        if (ans)
            cout << 0 << endl;
    }
}