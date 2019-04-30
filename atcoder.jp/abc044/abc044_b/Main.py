import sys
w = input()
for i in range(26):
    if w.count(chr(ord("a") + i)) % 2 != 0:
        print("No")
        sys.exit()
print("Yes")