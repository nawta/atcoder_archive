n = int(input())
d,x = list(map(int, input().split()))
for i in range(n):
	a = int(input())
	x += d // a + (d % a != 0)

print(x)