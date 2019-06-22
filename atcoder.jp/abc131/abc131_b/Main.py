import sys
n,l = list(map(int, input().split()))

if l >0:
    print(sum(range(l+1,l+n)))
elif l <=0:
    if l+n>0:
        print(sum(range(l,l+n)))
    else:
        print(sum(range(l,l+n-1)))
