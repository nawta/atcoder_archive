import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n,k = list(map(int, input().split()))

for i in range(1,k+1):
    if n-k+1 >= i:
        print(combinations_count(n-k+1,i)*combinations_count((k-i)+(i-1),(i-1)) % (10**9+7))
    else:
        print(0)