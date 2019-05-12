import sys
x = input()
n = [int(i) for i in list(x)]
x = int(x)
print("Yes" if x % sum(n) == 0 else "No")
