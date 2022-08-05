#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--){
        int n, m, a, n_zero = 0, m_zero = 0;
        cin >> n >> m;
        int an[n] = {0};
        int am[m] = {0};
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                cin >> a;
                if (a){
                    an[i]++;
                    am[j]++;
                }
            }
        }
        for (int i = 0; i < n; i++)
            if (an[i] == 0) n_zero++;  
        for (int i = 0; i < m; i++)
            if (am[i] == 0) m_zero++;
        
        if (min(n_zero, m_zero)%2)
            cout << "Ashish"  << endl;
        else
            cout << "Vivek"  << endl;

    }
}