n,k = list(map(int, input().split()))
r,s,p = list(map(int, input().split()))
t = input()

counter = 0
flag = -1

for i in range(k):
    flag = -1
    for j in range(i,n,k):
        if flag != 0 and t[j] == "r":
            flag = 0
            counter += p
            #print(counter,i,j,t[j])

        elif flag != 1 and t[j] == "s":
            flag = 1
            counter += r
            #print(counter,i,j,t[j])
            

        elif flag != 2 and t[j] == "p":
            flag = 2
            counter += s
            #print(counter,i,j,t[j])

        else:
            flag = -1

print(counter)