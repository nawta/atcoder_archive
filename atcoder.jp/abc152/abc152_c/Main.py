n = int(input())
p = list(map(int, input().split()))

imin = 2*(10**5) + 1
counter = 0

for i in range(len(p)):
    if imin > p[i]:
        counter += 1
        imin = p[i]

print(counter)