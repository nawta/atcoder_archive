a = int(input())
b = int(input())
c = int(input())
x = int(input()) /10
count =0

for ia in range(a,-1,-1):
    for ib in range(b,-1,-1):
        for ic in range(c,-1,-1):
            if ia*50 + ib*10 + ic*5 == x:
                count +=1
            elif ia*50 + ib*10 + ic*5 < x:
                break
        if ib >0 and ia*50 + (ib-1)*10 + c*5 < x:
            break
    if ia > 0 and (ia-1)*50 + b*10 + c*5< x:
        break
print(count)