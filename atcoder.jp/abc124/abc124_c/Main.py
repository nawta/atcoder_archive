import sys
s=input()
count =0
isSuccession = True #True:1 False:0
for i in range(len(s) -1):
    if s[i] != s[i+1]:
        if isSuccession == False:
            count +=1
    else:
        isSuccession = (isSuccession+1)%2
        if isSuccession == False:
            count +=1
print(min(count, len(s) - count))
                