n = int(input())
a =list(map(int, input().split()))
b =list(map(int, input().split()))
c =list(map(int, input().split()))

sum_satisfaction = 0

for i in range(n):
    sum_satisfaction += b[a[i]-1]
    if i == 0:
        continue
    elif a[i] == a[i-1] + 1:
        sum_satisfaction += c[a[i-1]-1]

print(sum_satisfaction)