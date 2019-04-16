import sys
n=int(input())
s=input()
str_ans = ""
for i in range((len(s)-1)//2 + 1):
    if i == 0:
        str_ans = "b"
    elif i %3 == 0:
        str_ans = "b" + str_ans + "b"
    elif i %3 == 1:
        str_ans = "a" + str_ans + "c"
    elif i %3 == 2:
        str_ans = "c" + str_ans + "a"
if str_ans == s:
    print((len(s)-1)//2)
else:
    print(-1)