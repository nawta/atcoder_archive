import sys
n,x = list(map(int, input().split()))
l = list(map(int, input().split()))
isum = 0
for i in range(1,n+1):
    isum += l[i-1]
    if isum > x:
        print(i)
        sys.exit()
print(n+1 if sum(l) <= x else i)