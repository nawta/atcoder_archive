n,k = list(map(int, input().split()))
s = input()

diff = 0

for i in range(n-1):
    if s[i] != s[i+1]:
        diff += 1

print(n - (diff - k*2) -1 if (diff - k*2) >= 0 else n-1)