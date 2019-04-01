n=int(input())
min=int(input())
for _ in range(n-1):
    a=int(input())
    if min > a:
        min = a
print(min)