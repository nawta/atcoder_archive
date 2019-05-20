n = int(input())
a = list(map(int, input().split()))

ave_a = sum(a) / n
dist = 1000007
flamenum = 0

for i in range(n):
    if abs(a[i] - ave_a) < dist:
        dist = abs(a[i] - ave_a)
        flamenum = i
        #print(dist)

print(flamenum)