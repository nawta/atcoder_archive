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
  
  int n,a,b,k,input;
  cin >> n >>a>>b>>k;
  std::vector<int> p;
  while(cin >> input){
    p.push_back(input);
  }
  p.push_back(a);  
  p.push_back(b);
  
  set<int> pp(p.begin(), p.end());
  
  if(p.size() == pp.size()){
    cout << "YES" << endl;
  }else{
    cout << "NO" << endl;
  }
  return 0;
}