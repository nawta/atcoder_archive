import sys
n = int(input())
w = []
for i in range(n):
    w.append(input())
if len(w) != len(set(w)):
    print("No")
    sys.exit()
for i in range(n-1):
    if w[i][len(w[i]) - 1] != w[i+1][0]:
        print("No")
        sys.exit()
print("Yes")