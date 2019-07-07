import sys

n = int(input())
a = list(map(int, input().split()))
x=[0]
for i in range(n):
    if i % 2 == 0:
        x[0] += a[i]
    else:
        x[0] -= a[i]

for i in range(n-1):
    tmp = 2*a[i] - x[i]
    x.append(tmp)

for i in range(n):
    print(x[i] ,end = " ")
print("")