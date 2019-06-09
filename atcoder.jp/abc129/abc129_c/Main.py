import sys
sys.setrecursionlimit(10**6)

def dfs(heights: int, a_index:int, a_n_1, a_n_2):
    if n < heights:
        return
    
    if m != 0 and a_index <= len(a) -1 and a[a_index] == heights:
        memo[2] = 0
        a_index += 1
        #print("10",heights)
    else:
        memo[2] = a_n_1 + a_n_2 #memo[1] + memo[0]
        #print("13",heights)
    dfs(heights+1,a_index,memo[2],a_n_1)
    return
    

n,m = list(map(int, input().split()))
memo = [1]*(3)
a = []
a_index = 0
if m != 0:
    for i in range(m):
        tmp = int(input())
        if i >= 1 and tmp -1 == a[len(a)-1]:
            print(0)
            sys.exit()
        else:
            a.append(tmp)
            #print(i,a)

    if a[0] == 1:
        memo[1] = 0
        a_index += 1
#a = list(set(a))
#a.sort()
dfs(2,a_index,memo[1],memo[0])
#print(memo)
print(memo[2] % (10**9+7))
