#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;


int main(){
  char c[4][4];
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      cin >> c[i][j];
    }
  }
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      cout << c[3-i][3-j]<< " ";
      if(j==3){
        cout << endl;
      }
    }
  }
  
  return 0;
}