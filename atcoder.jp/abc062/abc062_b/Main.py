import sys
h,w = list(map(int, input().split()))
a = []
for i in range(h):
    tmp = input()
    a.append(tmp)

print("#"*(w+2))

for j in range(h):
    print("#", end = "")
    print(a[j], end = "")
    print("#")

print("#"*(w+2))