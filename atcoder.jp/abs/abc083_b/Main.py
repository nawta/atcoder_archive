n,a,b = list(map(int, input().split()))
count=0

for i  in range(n+1):
    if a <= sum(list(map(int, list(str(i))))) <=b:
      count +=i
    
print(count)