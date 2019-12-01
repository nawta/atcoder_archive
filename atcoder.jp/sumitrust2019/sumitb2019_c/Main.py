x = int(input())

#imin = int(x/105)
imax = int(x/100)

if int(x%100) <=imax*5:
    print("1")
else:
    print("0")