#include <bits/stdc++.h>

using namespace std;

int main() {
    pair<int, int> a, b, c, d;

    cin >> a.first >> a.second;
    cin >> b.first >> b.second;
    cin >> c.first >> c.second;

    cout << 3 << endl;

    cout << + a.first + b.first - c.first << " " << + a.second + b.second - c.second << endl;
    cout << + a.first - b.first + c.first << " " << + a.second - b.second + c.second << endl;
    cout << - a.first + b.first + c.first << " " << - a.second + b.second + c.second << endl;
    // organizar pontos em sentido horário

    return 0;
}