#include <iostream>
#include <string>
#include <numeric>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int main(){
  int a,b;
  cin >> a >> b;
  int c= max(a,b);
  int d= min(a,b);
  cout << min(c-d, d+10-c) << endl;
  return 0;
}