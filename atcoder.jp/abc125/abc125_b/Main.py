import sys
n=int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
isum = 0
for i in range(n):
    if v[i] - c[i] >0:
        isum += v[i] - c[i]
print(isum)