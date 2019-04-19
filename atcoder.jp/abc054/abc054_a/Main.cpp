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
  
  int a,b;
  cin >> a >>  b;// >> c >> d;

  if (a == 1) a=14;
  if (b == 1) b=14;
  if(a>b){
    cout << "Alice" << endl;
  }
  else if(a<b){
    cout << "Bob" << endl;
  }
  else{
    cout << "Draw" << endl;
  }
  return 0;
}