a,b = list(map(int, input().split()))
s = input().split("-")
print("Yes" if len(s[0]) == a and len(s[1]) == b else "No")
