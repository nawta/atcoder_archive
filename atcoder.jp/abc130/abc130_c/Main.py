import decimal
w,h,x,y = list(map(int, input().split()))
print("{0:.9f}".format((w*h)/2),int((w/2) == x and (h /2) == y))