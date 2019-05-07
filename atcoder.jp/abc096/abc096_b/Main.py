import sys
import math

iabc= list(map(int, input().split()))
iabc.sort(reverse=True)
k = int(input())
print(iabc[0]*2**k + iabc[1] + iabc[2])