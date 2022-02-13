#include<bits/stdc++.h>
#define ff first
#define ss second

using namespace std;
using pii = pair<int, int>;
using ll = long long;

const ll oo = 1e18;

int main(){
    ll n, m, ans = oo, id=0, tm, sum = 0;
    cin >> n >> m;
    vector<ll> vs(n+1), ts(m);

    for (int i=0; i<n; i++){
        cin >> vs[i];
    }

    for (int i=0; i<m; i++){
        cin >> ts[i];
    }
    sort(ts.begin(), ts.end());
    // tm é a altura atual do professor
    tm = ts[0];
    vs[n] = tm;
    sort(vs.begin(), vs.end());

    // Achar onde está o tm na array ordenada
    for (int i=0; i<n+1; i++){
        if (vs[i] == tm) {
            id = i;
        }
        if (i&1) sum += abs(vs[i] - vs[i-1]);
    }

    ans = sum;
    for (int i=1; i<m; i++){
        tm = ts[i];
        // Aqui eu considerei que as duplas fossem identificadas pelo indice par
        // então para saber de qual dupla o indice pertence fiz (id/2)*2
        int tmp = (id/2)*2, j=id;

        // Atualiza a soma total
        sum -= abs(vs[tmp] - vs[tmp+1]);
        vs[id] = tm;
        sum += abs(vs[tmp] - vs[tmp+1]);
        ans = min(ans, sum);

        // Iteração para achar o lugar certo da nova altura inserida
        while (j<n and vs[j] > vs[j+1]){
            swap(vs[j], vs[j+1]);
            if (j&1){ // Atualiza se a posiçao é impar, pois a troca é entre duplas
                sum -= abs(vs[j-1] - vs[j+1]);
                sum += abs(vs[j-1] - vs[j]);
                sum -= abs(vs[j] - vs[j+2]);
                sum += abs(vs[j+1] - vs[j+2]);
                ans = min(ans, sum);
            }
            j++;
        }
        id = j;
    }

    cout << ans << endl;
}
