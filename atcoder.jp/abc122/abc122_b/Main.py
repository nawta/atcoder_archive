s=list(input())
counter=0
makkusu=0

for i in range(len(s)):
  if s[i] == "A" or s[i] == "T" or s[i] == "G" or s[i] == "C":
    counter +=1
    if counter > makkusu:
      makkusu = counter
  else:
    counter = 0
    
print(makkusu)