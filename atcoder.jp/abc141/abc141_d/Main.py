n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort(reverse=True)

while 1:
    a.sort(reverse=True)
    if m > 0:
        a[0] //= 2
        tmp_max = a[0] 
        m -=1
    if m == 0:
        break
    for i in range(1,n):
        if tmp_max <= a[i]:
            a[i] //= 2
            m -= 1
        if m == 0:
            break
print(sum(a))