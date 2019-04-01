#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int main(){
  int a;
  cin >> a;
  cout  << a%2 + a/2 << endl;
  if(a%2 == 1){
    cout  << a%2 << endl;
  }
  for(int i=0; i<a/2 ; i++){
    cout  << 2 << endl;
  }
  return 0;
}