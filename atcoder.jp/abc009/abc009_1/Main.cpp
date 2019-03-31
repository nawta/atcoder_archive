#include <iostream>
using namespace std;

int main(){
  int n;
  cin >> n;
  if(!cin.fail()){
    cout << n / 2 + n%2 << endl;
  }
}