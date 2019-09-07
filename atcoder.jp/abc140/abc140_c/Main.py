n = int(input())
b =list(map(int, input().split()))

isum = b[0]

for i in range(1,n-1):
    isum += min(b[i-1],b[i])
isum += b[n-2]
print(isum)
    