import math
a,b = list(map(int, input().split()))
s = int(str(a) + str(b))
sq = math.sqrt(s)
print("Yes" if sq - math.floor(sq) == 0 else "No"  )