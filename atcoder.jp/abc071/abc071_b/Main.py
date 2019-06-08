import sys

s = list(set(list(input())))
s.sort()
#print(s)
for i in range(len(s)):
    if s[i] != chr(ord("a") + i):
        print(chr(ord("a") + i))
        sys.exit()
if len(s) < 26:
  	print(chr(ord("a") + len(s)))
else:
	print("None")