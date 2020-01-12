n,m = list(map(int, input().split()))

problems = [0]*n
accurate = 0
penalty = 0

for i in range(m):
    p,s = input().split()
    p = int(p)

    if s == "AC" and problems[p-1] != -1:
         #初めて正解
         penalty += problems[p-1]
         accurate += 1
         problems[p-1] = -1
    elif s == "WA" and problems[p-1] != -1:
        #正解してない問題を不正解
        problems[p-1] += 1

print(accurate,penalty)