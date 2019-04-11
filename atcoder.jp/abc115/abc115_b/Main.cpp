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
  
  int N;
  cin >> N;
  int p[N];
  REP(i,N){
    cin >> p[i];
  }
  std::vector<int> v(p, p+N);
  //std::vector<int> data(10, 5);      //  要素数10、全ての要素の値5 で初期化
  //std::vector<int> data(123);  //  int 型で、初期要素数 123 の動的配列 data の宣言
  
  int imax = *max_element(v.begin(), v.end());
  int isum =0;
  REP(i,N){
    isum += v[i];
  }
  cout << isum - imax/2 << endl;
  return 0;
}