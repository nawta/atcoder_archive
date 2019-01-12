#include <stdio.h>

int main(){
	int N, H, W, ans;
	scanf("%d %d %d", &N, &H, &W);

	ans = (N-H+1)*(N-W+1);

	printf("%d", ans);


	return 0;
}