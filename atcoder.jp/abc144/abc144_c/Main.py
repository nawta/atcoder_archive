import sys
import math
n = int(input())
tmp = 10**12

for i in range(int(math.sqrt(n))+1, 0, -1):
    if n % i != 0:
        continue
    else:
        if tmp > (n//i)+(i)-2:
            tmp = (n//i)+i-2
print(tmp)