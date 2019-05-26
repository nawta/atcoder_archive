from operator import itemgetter
n = int(input())
s = [input().split() for i in range(n)]
for i in range(len(s)):
    s[i].append(i+1)
    s[i][1] = int(s[i][1])
s = sorted(s,key=lambda x:(x[0],-x[1]))

for i in range(n):
    print(s[i][2])