n = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
print(sum(s[::2]) - sum(s[1::2]))