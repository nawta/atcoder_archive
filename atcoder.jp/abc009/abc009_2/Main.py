n=int(input())
a=[int(input()) for _ in range(n)]
b=list(set(a))
b.sort(reverse = True)
print(b[1])