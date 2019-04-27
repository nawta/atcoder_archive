n,a,b = list(map(int, input().split()))
position=0
for i in range(n):
    s,d = input().split()
    d = int(d)
    if s == "West":
        if a <= d <= b:
            position -=d
        elif a>d:
            position -=a
        else:
            position -=b
    else:
        if a <= d <= b:
            position +=d
        elif a>d:
            position +=a
        else:
            position +=b
print("West " if position <0 else "East " if position >0 else "",end="")
print(abs(position))