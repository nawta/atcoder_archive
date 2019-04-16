n=int(input())
a=[]
for _ in range(n):
  a.append(int(input()))
print(len(a) - len(set(a)))
  
