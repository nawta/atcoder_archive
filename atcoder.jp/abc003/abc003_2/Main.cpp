#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;


int main(){
  string s,t;
  cin >> s >> t;
  for(int i=0; i<s.length() ; i++){
    if(s[i] != t[i]){
      if(s[i] == '@'){
        if(t[i] == 'a' ||t[i] == 't' ||t[i] == 'c' ||t[i] == 'o' ||t[i] == 'd' ||t[i] == 'e' ||t[i] == 'r'){
          s.erase(s.begin()+i);
          s.insert(s.begin()+i, t[i]);
        }
      }
      if(t[i] == '@'){
        if(s[i] == 'a' ||s[i] == 't' ||s[i] == 'c' ||s[i] == 'o' ||s[i] == 'd' ||s[i] == 'e' ||s[i] == 'r'){
          t.erase(t.begin()+i);
          t.insert(t.begin()+i, s[i]);
        }
      }
    }
  }
  
  if(s == t){
    cout << "You can win" << endl;
  }
  else{
    cout << "You will lose" << endl;
  }
  return 0;
}