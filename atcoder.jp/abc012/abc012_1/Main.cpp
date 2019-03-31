#include <iostream>
#include <string> 

using namespace std;
int main(){
  int a,b;
  cin >> a>>b;

  a = a^b;
  b = a^b;
  a = a^b;

  cout << a <<" "<< b<< endl;
  //cout << b <<" "<< a<< endl;でもokやけど…

  return 0;
}