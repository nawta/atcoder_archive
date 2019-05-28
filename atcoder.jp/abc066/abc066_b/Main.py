import sys
s = input()
s = s[:len(s)-1]
while 1:
    if len(s) %2 == 1:
        s = s[:len(s)-1]
        continue

    if s[:len(s) // 2] == s[len(s) // 2:]:
        print(len(s))
        sys.exit()
    else:
        s = s[:len(s)-1]