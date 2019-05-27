n,m = list(map(int, input().split()))
l_max = 1
r_min = n
for i in range(m):
    l,r = list(map(int, input().split()))
    if l > l_max:
        l_max = l
    if r < r_min:
        r_min = r
print(r_min-l_max+1 if r_min>=l_max else 0)