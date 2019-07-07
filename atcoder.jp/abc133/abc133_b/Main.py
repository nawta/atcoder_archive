import math

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

n,d = list(map(int, input().split()))
x = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    x.append(tmp)

counter = 0
distance = 0

for i in range(n-1):
    for j in range(i+1,n):
        distance = 0
        for k in range(d):
            distance += (x[i][k] - x[j][k])*(x[i][k] - x[j][k])
        #print(distance)
        distance = math.sqrt(distance)
        #print(x[i],x[j],distance)
        
        if is_integer_num(distance):
            #print("YES",distance)
            counter += 1

print(counter)