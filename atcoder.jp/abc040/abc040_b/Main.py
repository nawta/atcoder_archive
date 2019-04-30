n = int(input())
ans = 10**10
for x in range(1, n+1):
    y = max(n // x, 1)
    if x*y > n:
        continue
    ans = min(ans, abs(x - y) + n - x * y)
print(ans)
