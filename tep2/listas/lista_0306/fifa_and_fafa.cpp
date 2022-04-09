#include <bits/stdc++.h>

using namespace std;

const double PI = acos(-1.0);

int main() {
    double R, x1, y1, x2, y2, d, r, ang, xm, ym;

    cin >> R >> x1 >> y1 >> x2 >> y2;

    x2 -= x1; y2 -= y1;

    d = hypot(x2, y2);

    if (d >= R){
        // printf("menor\n");
        printf("%.8f %.8f %.8f", x1, y1, R);
        return 0;
    } 

    // cout << x2 << " " << y2 << endl;

    if (x2 == 0){
        // cout << "x2 == 0\n";
        if (y2 == 0){
            r = R/2;
            printf("%.8f %.8f %.8f", x1, y1+r, r);
        } else {
            r = (y2 + R)/2;
            if (y2 > 0) {
                printf("%.8f %.8f %.8f", x1, y1+y2-r, r);
            } else {
                printf("%.8f %.8f %.8f", x1, y1-y2+r, r);
            }
        }
        
        return 0;
    }

    ang = atan(abs(y2)/abs(x2));
    r = (d + R)/2;

    // cout << R*cos(ang) << " " << R*sin(ang) << endl;
    if (x2 > 0 && y2 >= 0){
        xm = (x2-R*cos(ang))/2; 
        ym = (y2-R*sin(ang))/2;
    } else if (x2 > 0 && y2 < 0) {
        xm = (x2-R*cos(ang))/2; 
        ym = (y2+R*sin(ang))/2;
    } else if (y2 >= 0) {
        xm = (x2+R*cos(ang))/2; 
        ym = (y2-R*sin(ang))/2;
    } else {
        xm = (x2+R*cos(ang))/2; 
        ym = (y2+R*sin(ang))/2;
    }

    // cout << xm << " " << ym << endl;
    printf("%.8f %.8f %.8f", x1+xm, y1+ym, r);

    return 0;
}