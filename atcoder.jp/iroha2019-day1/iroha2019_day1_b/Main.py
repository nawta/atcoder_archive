s=input()
k=int(input()) % len(s)
print(s[k:] + s[:k])
