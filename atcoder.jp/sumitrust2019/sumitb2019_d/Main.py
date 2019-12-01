n = int(input())
s = input()

imemo = [0]*10
memo = [0]*100
counter = 0

for i in range(n):
    if imemo[int(s[i])] == 0:
        imemo[int(s[i])] = 1
    else:
        continue
        
    for j in range(i+1,n):
        if memo[int(s[i])*10+int(s[j])] == 0:
                memo[int(s[i])*10+int(s[j])] = 1
                counter += len(set(s[j+1:]))
print(counter)
