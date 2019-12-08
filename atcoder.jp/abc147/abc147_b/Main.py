s = input()
counter = 0

for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        counter += 1
print(counter)