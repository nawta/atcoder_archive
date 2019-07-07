import sys

l,r = list(map(int, input().split()))
imin = 10**9+7

if r-l+1 <=2019:
    for i in range(l,r):
        for j in range(i+1,r+1):
            if imin > (i*j)%2019:
                imin = (i*j)%2019
    print(imin)
else:
    print(0)