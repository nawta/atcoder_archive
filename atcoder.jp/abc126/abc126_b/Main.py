import sys
s = int(input())
a = s //100
b = s % 100
mmyy = 0
yymm = 0

if 1<=a <= 12:
    if 1<=b <= 12:
         yymm = 1
         mmyy = 1
    else:
        mmyy = 1
elif 0 <= a <= 99:
    if 1<=b <= 12:
         yymm = 1

if mmyy == 1 and yymm == 1:
    print("AMBIGUOUS")
elif mmyy == 1:
    print("MMYY")
elif yymm == 1:
    print("YYMM")
else:
    print("NA")