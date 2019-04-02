ia=int(input())
imax=0
for x in range(1,ia):
    if x*(ia-x)>imax:
        imax=x*(ia-x)
print(imax)