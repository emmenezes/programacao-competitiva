#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    int n, H, M, min_h, min_m, h, m, aux_h, aux_m;
    cin >> t;

    while(t--){
        cin >> n >> H >> M;
        min_h = 24; min_m = 60;
        while (n--){
            cin >> h >> m;
            if (H > h){
                if (M > m){
                    aux_h = h - H + 23;
                    aux_m = m - M + 60;
                } else {
                    aux_h = h - H + 24;
                    aux_m = m - M;
                }
            } else {
                if (M > m){
                    aux_h = h - H - 1;
                    aux_m = m - M + 60;
                    if (aux_h < 0)
                        aux_h = 23;
                } else {
                    aux_h = h - H;
                    aux_m = m - M;
                }
            }
            if (aux_h < min_h){
                min_h = min(min_h, aux_h);
                min_m = aux_m;
            } else if (aux_h == min_h)
                min_m = min(min_m, aux_m);
        }
        cout << min_h << " " << min_m << endl;
    }

}