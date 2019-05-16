import sys
n,goalA,goalB,goalC = list(map(int, input().split()))
l = [int(input()) for _ in range(n)]
cost = []
isum = 0

def dfs(depth: int, a: int, b: int, c:int, isum:int):
    if depth == n:
        if min(a,b,c) > 0:
            cost.append(abs(a - goalA) + abs(b - goalB) + abs(c - goalC) +isum - 30)
            return
        else:
            cost.append(10**8)
            return
    
    dfs(depth+1, a, b, c, isum)
    dfs(depth+1, a + l[depth], b, c, isum + 10) 
    dfs(depth+1, a , b + l[depth], c, isum+10) 
    dfs(depth+1, a , b, c + l[depth], isum + 10) 
    

dfs(0,0,0,0,isum)
print(min(cost))