n=int(input())
ist = []

ist.append(input().split())

#print(type(ist[::2]))
#print(type(ist[1::2]))
for i in ist:
    ist = list(map(int, i))
    
ist.sort(reverse=True)
print(int(sum(ist[::2])) - int(sum(ist[1::2])))