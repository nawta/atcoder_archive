#include <iostream>
#include <string>
#include <numeric>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int main(){
  int a;
  cin >> a;
  printf("%02d:", a/3600);
  printf("%02d:", (a%3600)/60);
  printf("%02d\n", (a%3600)%60);
  return 0;
}