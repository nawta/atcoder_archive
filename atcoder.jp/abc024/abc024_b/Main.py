n,t = list(map(int, input().split()))
a = [int(input()) for i in range(n)]
isum=0
for i in range(n-1):
    if a[i]+t <= a[i+1]:
        isum += t
        #print(i,isum)
    else:
        isum += a[i+1] - a[i]
        #print(i,isum)
print(isum+t)
