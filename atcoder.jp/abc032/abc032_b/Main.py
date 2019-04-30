import sys
s=input()
k=int(input())
password_option = []
if k > len(s):
    print(0)
    sys.exit()
else:
    for i in range(len(s) -k +1):
        if all(password_option[j] != s[i:i+k] for j in range(len(password_option))):
            password_option.append(s[i:i+k])
print(len(password_option))
