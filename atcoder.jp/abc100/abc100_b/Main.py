import sys
d,n = list(map(int, input().split()))
if d == 1:
    print((n+(n == 100))*100)
elif d == 2:
    print((n+(n == 100))*100*100 )
else:
    print(n if n != 100 else 101)