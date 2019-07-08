import sys
n = int(input())
k = int(input())
x = list(map(int, input().split()))

isum = 0

for i in range(n):
    isum += min(x[i], k-x[i])

print(isum*2)