import sys

def search_next(nextbutton : int) -> int:
    nextbutton = a.index(nextbutton) +1
    return nextbutton

n = int(input())
a = [int(input()) for i in range(n)]
nextbutton = 1
count = 0

#print(nextbutton,"first")

for _ in range(n):
    if nextbutton == 2:
        print(count)
        #print(nextbutton,"1")
        
        sys.exit()
    else:
        nextbutton = a[nextbutton -1]
        #print(nextbutton,"el")
        
        count += 1
print(-1)