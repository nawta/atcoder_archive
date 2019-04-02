#include <iostream>
#include <string>
#include <numeric>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int main(){
  int n,X,a,sum=0;
  cin >> n >> X;
  for(int i=0;cin>>a; i++){
    if((X>>i) & 1){
      sum += a;
    }
  };
  cout << sum << endl;
  return 0;
}