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
  std::vector<int> r;
  cin>> n;
  REP(i,n){
    int tmp;
    cin >> tmp;
    r.push_back(tmp);
  }
  sort(r.begin(),r.end(),std::greater<int>());
  int isum=0;
  int operand = 1;
  REP(i,n){
    isum += pow(r[i],2)*(operand);
    if(operand==1){
      operand=-1;
    }else{
      operand=1;
    }
  }
  cout <<std::fixed<<std::setprecision(10) << isum*M_PI << endl;
  return 0;
}