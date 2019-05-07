import sys
import math

a,b,k = list(map(int, input().split()))
if b-a+1 <= k:
    for i in range(a,b+1):
        print(i)
else:
    lis = list(range(a,a+k))
    lis.extend(list(range(b-k+1, b+1)))
    lis = list(set(lis))
    lis.sort()
    for i in range(len(lis)):
        print(lis[i])