#include <bits/stdc++.h>
#define ll long long
#define INIT std::ios::sync_with_stdio(false);std::cin.tie(0);
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

using namespace std;
int main() {
  INIT;
  
  int a,b,c;
  cin >> a >> b >> c;
  if(a+b+c == 17 && (a == 5 || a == 7) && (b == 5 || b == 7) && (c == 5 || c == 7) ){
    cout << "YES" << endl;
  }else{
    cout << "NO" << endl;
  }
  
  return 0;
}