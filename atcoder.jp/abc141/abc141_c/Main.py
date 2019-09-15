n,k,q = list(map(int, input().split()))
a = [0]*n
for i in range(q):
    tmp = int(input())
    a[tmp-1] += 1

b = ["No"]*n
    

for i in range(n):
    if k - q + a[i] > 0 :
        b[i] = "Yes"

for i in range(n):
    print(b[i])