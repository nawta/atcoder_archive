import sys
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

x = int(input())

if x == 2:
    print(x)
    sys.exit()

for i in range(x, 10**5+4):
    if i % 2 == 1 and is_prime(i):
        print(i)
        sys.exit()