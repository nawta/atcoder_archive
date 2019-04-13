import sys
a,b=list(map(int, input().split()))
count=max(a,b)
if a >= b:
    a -=1
else:
    b -=1
count +=max(a,b)
print(count)