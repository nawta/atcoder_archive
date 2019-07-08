import sys
s = input()
t = input()

for i in range(len(s)):
    if s == t:
        print("Yes")
        sys.exit()
    else:
        tmp = s[0]
        s = s[1:] + tmp
print("No")