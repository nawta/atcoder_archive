import sys
n,m,X,Y = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z=[]
for i in range(-100,101):
    if X < i <= Y:
        z.append(i)
for i in range(len(z)):
    if max(x) < z[i] <= min(y):
        print("No War")
        sys.exit()
print("War")