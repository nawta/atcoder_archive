s = input()
ans = ""
for i in range(len(s)):
    if s[i] == "0":
        ans = ans + "0"
    elif s[i] == "1":
        ans = ans + "1"
    elif s[i] == "B":
        ans = ans[:len(ans)-1]
print(ans)