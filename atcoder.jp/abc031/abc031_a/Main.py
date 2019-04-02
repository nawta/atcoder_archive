ia,id=list(map(int, input().split()))
if (ia+1)*id >= ia*(id+1):
    print((ia+1)*id)
else:
    print(ia*(id+1))