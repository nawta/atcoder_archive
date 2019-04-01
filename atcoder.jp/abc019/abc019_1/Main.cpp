#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int main(){
  std::vector<int> v;
  int a;
  while(cin >> a){
    v.push_back(a);
  }
  sort(v.begin(), v.end());
  cout << v[1] << endl;
  return 0;
}