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
  
  int n,h;
  int count =0;
  cin >> n >> h;
  int a[n],b[n];
  REP(i,n){
    cin >> a[i] >> b[i];
  }
  std::vector<int> va(a, a+n);

  int imax = *std::max_element(va.begin(), va.end());
  int suffix;
  REP(i,n){
    if(a[i] == imax){
      suffix = i;
      break;
    }
  }

  std::vector<int> vb(b, b+n);
  sort(vb.begin(), vb.end(),std::greater<int>());

  REP(i,n){
    if(vb[i] < imax){
      break;
    }
    h -= vb[i];
    count +=1;
    if(h <= 0){
      printf("%d\n", count);
      exit(0);
    }
  }

  while (1) {
    h -= imax;
    count++;
    if(h <= 0){
      printf("%d\n", count);
      exit(0);
    }
  }

/*
  // vの全ての要素にdisp()関数を適用する
  std::for_each(v.begin(), v.end(), disp);
  
  // 要素の内容を書き換えても構わないし、呼び出し順序に依存した処理を書いても構わない
  std::for_each(v.begin(), v.end(), mutate());
  std::for_each(v.begin(), v.end(), disp);
  
  */
  return 0;
}