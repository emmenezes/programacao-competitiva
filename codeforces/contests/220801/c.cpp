#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n, max_n;

    cin >> t;
    while(t--) {
        set<int> ans;
        cin >> n;
        max_n = 9;
        while (n > max_n){
            ans.insert(max_n);
            n -= max_n;
            max_n--;
        }
        if (n)
            ans.insert(n);
        
        auto it = ans.begin();
        for (; it != ans.end(); it++){
            cout << *it;
        }
        cout << endl;

    }
}