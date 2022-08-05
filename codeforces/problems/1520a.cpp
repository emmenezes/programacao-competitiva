#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        string s;
        bool ans = true;
        cin >> n;
        cin >> s;
        set<char> ref_set;
        ref_set.insert(s[0]);
        char ref = s[0];
        for (int i = 1; i < n; i++) {
            if (ref != s[i]) {
                if (ref_set.find(s[i]) != ref_set.end()) {
                    ans = false;
                    break;
                } else {
                    ref_set.insert(s[i]);
                    ref = s[i];
                }
            }
        }
        if (ans)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
}