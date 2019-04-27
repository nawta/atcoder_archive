import sys
x,y = list(input().split())
judge = 0
x = x.translate(str.maketrans({"3":"1","5":"1","7":"1","8":"1","6":"4","9":"4"}))
y = y.translate(str.maketrans({"3":"1","5":"1","7":"1","8":"1","6":"4","9":"4"}))
x = x.replace("10", "1").replace("12", "1").replace("11","4")
y = y.replace("10", "1").replace("12", "1").replace("11","4")

print("Yes" if x == y else "No")

