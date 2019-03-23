s = int(input())
l = [s]
max=s
 
while 1:
  if s %2 == 0:
    l.append(s/2)
    s = int(s/2)
  else:
    l.append(3*s + 1)
    s = 3*s+1
    max = s
  
  if any(l.count(i) >= 2 for i in range(s+1)):
    print(len(l))
    break