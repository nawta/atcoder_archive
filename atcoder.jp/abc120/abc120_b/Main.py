a,b,k = list(map(int, input().split()))
x=[]

for i in range(1, min(a, b)+1):
    if a%i == 0 and b%i==0:
      x.append(i)

x.sort(reverse=True)
print(x[k-1])