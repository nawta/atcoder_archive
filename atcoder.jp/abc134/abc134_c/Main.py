n = int(input())
a = [int(input()) for _ in range(n)]

imax = max(a)
b = sorted(a)
#print(imax)
for i in range(n):
    if not a[i] == imax:
        print(imax)
    else:
        print(b[n-2])