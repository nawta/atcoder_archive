s=input()
imin = 753
for i in range(len(s)-2):
  if abs(int(s[i]+s[i+1]+s[i+2]) - 753) < imin:
    imin = abs(int(s[i]+s[i+1]+s[i+2]) - 753)
print(imin)