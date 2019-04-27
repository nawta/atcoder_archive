#include <bits/stdc++.h>
#define ll long long
#define INIT std::ios::sync_with_stdio(false);std::cin.tie(0);
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

using namespace std;

int gcd(int x, int y) {
  if (y == 0)return x;
  return gcd(y, x%y);
}

int main() {
  INIT;
  
  int n,count=0;
  std::vector<ll> a;
  cin >> n;
  REP(i,n){
    ll f;
    cin >>f;
    if(f < 0){
      count++;
      f = -f;
    }
    a.push_back(f);
  }
  
  sort(a.begin(), a.end());
  
  if(count % 2 == 0){
    cout << accumulate(a.begin(), a.end(), 0LL) << endl;
  }else{
    cout << accumulate(a.begin()+1, a.end(), 0LL) - a[0] << endl;
  }
  
  return 0;
}