#include <iostream>
#include <string> 
#include <vector>

using namespace std;
int main(){
  int a, b, sum=0;

  for(int i=0; i<3; i++){
    cin >> a >>b;
    sum += a*b/10; 
  }
  cout << sum << endl;
  
  return 0;
}