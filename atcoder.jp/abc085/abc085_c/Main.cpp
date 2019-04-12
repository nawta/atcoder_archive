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
  
  int n,y;
  cin >> n >> y;
  
  y = y/1000;
  REP(i, y/10 + 1){
    REP(j, y/5 + 1){
      REP(k, y + 1){
        if(10*i + 5*j + k == y && i+j+k==n){
          printf("%d %d %d", i, j, k);
          exit(0);
        }
        else if(10*i + 5*j + k > y || i+j+k>n){
          break;
        }
      }
      if(10*i + 5*j > y || i+j>n){
        break;
      }
    }
    if(10*i > y || i>n){
      break;
    }
  }
  printf("-1 -1 -1");
  return 0;
}