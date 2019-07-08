n = int(input())
s = input()
isum = 0
imax = 0

for i in range(n):
    if s[i] == "I":
        isum += 1
        if imax < isum:
            imax = isum
    else:
        isum -= 1
print(imax)