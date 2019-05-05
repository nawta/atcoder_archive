import sys
n = int(input())
s = input()
count_max = 0
for i in range(1,n):
    if len(set(s[:i]) & set(s[i:])) >count_max:
        count_max = len(set(s[:i]) & set(s[i:]))
print(count_max)