import math
n = int(input())
z = []
isum = 0
for _ in range(n):
    z.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            isum += math.factorial(n-1)*math.sqrt((z[i][0] - z[j][0])*(z[i][0] - z[j][0]) + (z[i][1] - z[j][1])*(z[i][1] - z[j][1]))
            #print(i,j,isum)

print(isum/math.factorial(n))