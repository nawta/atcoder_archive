n,k,m = list(map(int, input().split()))
a = list(map(int, input().split()))

isum = sum(a)
if (m*n-isum) <= 0:
    print(0)
elif 0 < (m*n-isum) <= k:
    print(m*n-isum)
else:
    print(-1)