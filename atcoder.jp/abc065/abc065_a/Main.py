x,y,z= list(map(int, input().split()))
if y>=z:
    print("delicious")
else:
    print("safe" if x+y>=z else "dangerous")
