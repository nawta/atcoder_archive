import sys
import math

n,m,x = list(map(int, input().split()))
a = list(map(int, input().split()))
former_count = 0
for i in range(m):
    if a[i] < x:
        former_count +=1
    else:
        break
print(min(former_count, m - former_count))