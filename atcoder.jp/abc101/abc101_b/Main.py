import sys
n = input()
N = int(n)
n = [int(i) for i in list(n)]
print("Yes" if N % sum(n) == 0 else "No")