import sys
s = int(input())
for i in range(10):
    if i*100+i*10+i< s <= (i+1)*100+(i+1)*10+(i+1):
        print((i+1)*100+(i+1)*10+(i+1))
        sys.exit()