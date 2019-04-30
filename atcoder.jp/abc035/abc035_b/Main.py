s=input()
t=int(input())
vertical=0
horizontal= 0
secret_counter = 0
for i in range(len(s)):
    if s[i] == "U":
        vertical += 1
    elif s[i] == "D":
        vertical -= 1
    elif s[i] == "L":
        horizontal += 1
    elif s[i] == "R":
        horizontal -= 1
    else:
        secret_counter += 1
if t == 1:
    print(abs(horizontal) + abs(vertical) + secret_counter)
else:
    if secret_counter < abs(horizontal) + abs(vertical):
        print(abs(horizontal) + abs(vertical) - secret_counter)
    else:
        if (secret_counter - (abs(horizontal) + abs(vertical))) % 2:
            print(1)
        else:
            print(0)