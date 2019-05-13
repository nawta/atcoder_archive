import copy
n,m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()
#print(a)

money = 0
for i in range(n):
    for j in range(a[i][1]):
        money += a[i][0]
        m -= 1
        #print(money,m,a)
        if m == 0:
            break
    if m == 0:
        break
print(money)