#include <bits/stdc++.h>

using namespace std;

int main() {
    string s, t;

    cin >> s;
    cin >> t;

    int st = s.size();
    int tt = t.size();
    int m = tt;

    for (int i = 0; i <= st-tt; i++) {
        int c = 0;
        for (int j = 0; j < tt; j++){
            if (s[i+j] != t[j])
                c++;
        }
        if (c < m)
            m = c;
    }
    
    cout << m << endl;



    return 0;
}