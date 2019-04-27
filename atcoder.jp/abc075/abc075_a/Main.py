a,b,c = list(map(int, input().split()))
print(a*(b == c) +b*(a == c) +c*(b == a) )