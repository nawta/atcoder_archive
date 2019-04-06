a=[int(input()) for _ in range(5)]
one = 10
for i in range(5):
    if a[i] % 10 != 0 and a[i]%10 <one:
        one = a[i]%10
for i in range(5):
    if a[i] % 10 == 0:
        a[i] = a[i] // 10
    else:
        a[i] = a[i] // 10 + 1
print(sum(a)*10 -10 +one) 