#include <iostream>
#include <string>
#include <numeric>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int Gcd(int x, int y){
    int r;
    if(x == 0 || y == 0){
        cerr << "Error: argument of Gcd" << endl;
    }
    while((r = x % y) != 0){
        x = y;
        y = r;
    }
    return y;
}

int main(){
  int a, b, n, k=1;
  cin >> a >> b >> n;
  int z = a*b / Gcd(a,b);
  for(int i=n; ;){
    if(i<= z*k){
      break;
    }else{
      k++;
    }
  }
  cout<<z*k<<endl;
  return 0;
}
