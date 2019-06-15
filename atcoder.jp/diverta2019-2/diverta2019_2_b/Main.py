import sys
import collections
n = int(input())
z = [list(map(int, input().split())) for _ in range(n)]
z.sort()
pq_pattern = []
pq_counter = [1]*(n-1)*n

if n == 1:
    print(1)
    sys.exit()

for i in range(n):
    for j in range(n):
        if not i == j:
            if [z[j][0] - z[i][0], z[j][1] - z[i][1]] in pq_pattern:
                #print("YES!")
                pq_counter[pq_pattern.index([z[j][0] - z[i][0], z[j][1] - z[i][1]])] += 1
            else:
                pq_pattern.append([z[j][0] - z[i][0], z[j][1] - z[i][1]])
print(n-max(pq_counter))