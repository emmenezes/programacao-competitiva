#include<bits/stdc++.h>
#define ff first
#define ss second

using namespace std;
using pii = pair<int, int>;
using ll = long long;
using ld = long double;

const ll oo = 1e18;
const ll maxn = 110;

vector<int> parent(maxn);

struct point {
    ld x, y;
};

void init(){
    for (int i=0; i<maxn; i++){
        parent[i] = i;
    }
}

int find(int x){
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void join(int a, int b){
    a = find(a);
    b = find(b);

    if (a == b) return;

    parent[a] = b;
}

bool same(int a, int b){
    a = find(a);
    b = find(b);

    return a == b;
}

ld dist(point a, point b){
    return hypot(a.x - b.x, a.y - b.y);
}

int main(){
    init();
    int n;
    cin >> n;

    vector<point>vs(n);
    vector<pair<ld, pii>>ts;

    for (int i=0; i<n; i++){
        cin >> vs[i].x >> vs[i].y;
    }

    for (int i=0; i<n; i++){
        for (int j=i+1; j<=n+1; j++){
            point a = vs[i], b;
            // Se o indice é n+1, então é considerado o ponto mais próximo da parede inferior
            if (j == n+1) b = {a.x, -100}; 
            // Se o indice é n, então é considerado o ponto mais proximo da parede superior
            else if (j == n) b = {a.x, 100};
            else b = vs[j];

            ts.push_back({dist(a, b), {i, j}});
        }
    }
    sort(ts.begin(), ts.end());
    ld last = -1, i = 0;
    while (!same(n, n+1)){ // Se a parede ainda não fechou a passagem
        last = ts[i].ff;
        join(ts[i].ss.ff, ts[i].ss.ss);
        i++;
    }

    cout << fixed << setprecision(20) << last/2 << endl;
}