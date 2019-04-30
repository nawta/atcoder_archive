n,q=list(map(int, input().split()))
a = [0]*n
for i in range(q):
    l,r,t = list(map(int, input().split()))
    for j in range(r-l+1):
        a[l-1+j] = t

for i in range(n):
    print(a[i])