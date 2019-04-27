a,b,c,d = list(map(int, input().split()))
print("Yes" if abs(a-c)<= d or abs(a-b)<=d and abs(c-b) <= d else "No")