import sys
n = int(input())
w = list(map(int, input().split()))
imin = 10000
for i in range(n-1):
    if abs(sum(w[:i+1]) - sum(w[i+1:])) < imin:
        imin = abs(sum(w[:i+1]) - sum(w[i+1:]))
print(imin)