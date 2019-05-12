n,a,b = list(map(int, input().split()))
isum = 0
for i in range(1,n+1):
    tmp = [int(j) for j in list(str(i))]
    #print(tmp,sum(tmp))
    if a <= sum(tmp) <= b:
        isum += i
print(isum)