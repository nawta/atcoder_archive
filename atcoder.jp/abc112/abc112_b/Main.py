import sys
n,t = list(map(int, input().split()))
imincost=1001
for _ in range(n):
    c_,t_ = list(map(int, input().split()))
    if t_ <= t and c_ <imincost:
        imincost = c_
print(imincost if imincost != 1001 else "TLE")