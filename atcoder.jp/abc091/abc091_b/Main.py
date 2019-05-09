n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

sset = list(set(s))
imax = 0
for i in range(len(sset)):
    if imax < s.count(sset[i]) - t.count(sset[i]):
        imax = s.count(sset[i]) - t.count(sset[i])
print(imax)