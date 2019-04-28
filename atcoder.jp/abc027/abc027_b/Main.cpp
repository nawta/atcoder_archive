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
  
  int n;
  std::vector<int> a;
  cin>> n;
  REP(i,n){
    int tmp;
    cin >> tmp;
    a.push_back(tmp);
  }
  int isum =accumulate(a.begin(), a.end(), 0);
  if(isum % n != 0){
    cout << -1 << endl;
    return 0;
  }
  int bridge_count =0;
  int ave = isum /n;
  REP(i,n-1){
    if(accumulate(a.begin(),a.begin()+i+1,0) != ave*(i+1)) bridge_count++;
  }
  cout <<bridge_count<< endl;
  return 0;
}