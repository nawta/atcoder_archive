#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;
int main(){
  float a;
  cin >> a ;
  a = a/1000;
  if(a<0.1){
    cout  << "00" << endl;
  }
  else if(0.1<=a && a<=5){
    printf("%02d\n", (int)(a*10));
  }
  else if(6<=a && a<=30){
    cout  << (int)a + 50 << endl;
  }
  else if(35<=a && a<=70){
    cout  << (int)((a-30)/5) +80 << endl;
  }
  else if(70<a){
    cout  << 89 << endl;
  }
  return 0;
}