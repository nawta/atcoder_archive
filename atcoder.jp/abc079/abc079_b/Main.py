import sys
n = int(input())
memo =[2,1]
for i in range(2,n+1):
    memo.append( memo[i-1]+memo[i-2] )
print(memo[n])
