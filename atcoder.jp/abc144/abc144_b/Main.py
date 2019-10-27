import sys
n = int(input())

for i in range(1,10):
    tmp = n //i
    mod = n % i
    if 1<=tmp<=9 and mod == 0:
        print("Yes")
        sys.exit() 
    else:
        continue
print("No")