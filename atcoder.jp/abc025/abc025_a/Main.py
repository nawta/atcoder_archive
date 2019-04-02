import itertools
s=list(input())
n=int(input())
k=list(itertools.product(s,s))
#print(k[n-1][0]+k[n-1][1])
print(''.join(k[n-1]))