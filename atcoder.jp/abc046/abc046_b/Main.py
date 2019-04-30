import sys
n,k = list(map(int, input().split()))
combination = k
for i in range(n-1):
    combination *= k-1
print(combination)