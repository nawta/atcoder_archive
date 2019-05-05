import sys
a,b = list(map(int, input().split()))
heights_a = 0
for i in range(1,b-a):
    heights_a += i
print(heights_a - a)