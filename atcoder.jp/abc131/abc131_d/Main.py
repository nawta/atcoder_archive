import sys
n = int(input())
a= [list(map(int, input().split())) for i in range(n)]

a.sort(key = lambda x: x[1])

sum = 0

for i in range(n):
    if i == 0:
        a[i][0] += 0
    else:
        a[i][0] += a[i-1][0]
    sum += a[i][0]

for i in range(n):
    if a[i][0] > a[i][1]:
        print("No")
        sys.exit()
print("Yes")