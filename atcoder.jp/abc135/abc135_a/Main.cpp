#include <bits/stdc++.h>
using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;
    long long dif = abs(a- b);
    if(dif % 2 == 1) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        cout << dif / 2 + min(a, b) << endl;
    }
}