n=int(input())
kane=0

for _ in range(n):
  x, u= input().split()
  if u == "JPY":
    kane +=int(x)
  elif u == "BTC":
    kane += 380000.0*float(x)
    
print(kane)