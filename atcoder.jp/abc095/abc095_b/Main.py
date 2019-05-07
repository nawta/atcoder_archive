import sys
import math

n,x = list(map(int, input().split()))
m = [int(input()) for i in range(n)]
x -= sum(m)
count = 0
while 1:
    if x < min(m):
        break
    else:
        x -= min(m)
        count+=1
print(count + n)