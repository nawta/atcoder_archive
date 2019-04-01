#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

void strReplace (std::string& str, const std::string& from, const std::string& to) {
    std::string::size_type pos = 0;
    while(pos = str.find(from, pos), pos != std::string::npos) {
        str.replace(pos, from.length(), to);
        pos += to.length();
    }
}
int main(){
  string a;
  cin >> a ;
  strReplace(a, "a", "");
  strReplace(a, "i", "");
  strReplace(a, "u", "");
  strReplace(a, "e", "");
  strReplace(a, "o", "");

  cout << a << endl;
  
  return 0;
}