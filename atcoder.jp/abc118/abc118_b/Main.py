n,m = list(map(int, input().split()))
counter = [0]*m
#min = m

for i in range(n):
  k,*b = input().split()
  b = [int(j) for j in b]
  for l in b:
    counter[l-1] +=1
    
print(counter.count(n))