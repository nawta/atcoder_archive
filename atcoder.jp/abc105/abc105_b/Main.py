import sys
n = int(input())
n2 = n
while n>0:
    if n % 4 == 0 or n % 7 == 0:
        print("Yes")
        sys.exit()
    n -= 7
while n2>0:
    if n2 % 4 == 0 or n2 % 7 == 0:
        print("Yes")
        sys.exit()
    n2 -= 4
print("No")