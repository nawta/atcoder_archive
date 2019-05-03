import sys
s = input()
judge = 0
if s[0] == "A":
    judge += 1

if s[1] != "C" and s[len(s) -1] != "C" and s.count("C") == 1:
    judge += 1

s = s.replace("A","a").replace("C","c")
#print(s,judge)
if s.islower() and judge == 2:
    print("AC")
else:
    print("WA")