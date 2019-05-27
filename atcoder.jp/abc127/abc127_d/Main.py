n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]
bc.sort(reverse = True, key = lambda x: x[1])
i = 0
counter = 0
while 1:
    for j in range(bc[i][0]):
        a.append(bc[i][1])
        counter += 1
        if counter == n:
            break
    if counter == n or i == len(bc)-1:
        break
    i += 1

a.sort(reverse = True)
print(sum(a[:n]))
