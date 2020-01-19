a,b = list(map(int, input().split()))
tmp = str(a)*b
tmp2 = str(b)*a

print(min(tmp,tmp2))