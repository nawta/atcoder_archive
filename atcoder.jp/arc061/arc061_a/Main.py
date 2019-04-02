s=input()
a = s
isum=0
k=0
for i in range(2**(len(s)-1)):
    for j in range(len(s)-1):
        if ((i>>j) & 1):
            #print(bin(i))
            a = a[:j+k+1] + "+" + a[j+k+1:]
            k +=1
            #print(a,j)
    k=0
    isum += sum(list(map(int, a.split("+"))))
    a=s
print(isum)