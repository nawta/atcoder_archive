a=list(map(int,input().split()))
a.sort(reverse=True)

print(int(str(a[0])+str(a[1]))+int(a[2]))