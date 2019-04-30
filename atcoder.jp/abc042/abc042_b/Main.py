n,l = list(map(int, input().split()))
s = []
for i in range(n):
    tmp = input()
    s.append(tmp)
s.sort()
for i in range(n):
    print(s[i], end = "")
print()