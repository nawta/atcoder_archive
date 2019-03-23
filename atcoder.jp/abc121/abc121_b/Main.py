n,m,c=list(map(int,input().split()))
b=list(map(int,input().split()))
counter=0
 
for _ in range(n):
  a=list(map(int,input().split()))
  x = [a[i]*b[i] for i in range(m)]
  if sum(x)+c > 0:
    counter +=1
    
print(counter)