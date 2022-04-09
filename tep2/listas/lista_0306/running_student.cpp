#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, min; 
    long double vb, vs, t = 1000000, temp, x[100], xu, yu;
    
    cin >> n >> vb >> vs;

    for (int i = 0; i < n; i++)
        cin >> x[i];
    
    cin >> xu >> yu;

    for (int i = 1; i < n; i++){
        temp = 0;
        temp = x[i]/vb + sqrt(pow(x[i] - xu, 2) + pow(yu,2))/vs;

        // cout << x[i] << " " << x[i]/vb << " " << ((x[i] - xu)^2) << " " << sqrt((x[i] - xu)^2 + yu^2) << " " << ((x[i] - xu)^2) << endl;
        // cout << temp << endl << endl;
        if (temp <= t){
            if (temp == t){
                if (pow(x[i] - xu,2) < pow(x[min] - xu,2))
                    min = i;
            } else {
                t = temp;
            min = i;
            }
        }
            
    }

    cout << min + 1<< endl;

    return 0;
}