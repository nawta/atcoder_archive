import sys
import math
a,b,x = list(map(int, input().split()))

if a*a*b/2 < x:
    print(180*math.atan(2*b/a-2*x/a/a/a)/math.pi)
else:
    print(math.atan(a*b*b/2/x)*180/math.pi)