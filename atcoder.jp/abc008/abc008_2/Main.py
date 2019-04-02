from collections import Counter
N = int(input())
S = [input() for i in range(N)]
c = Counter(S).most_common()
print(c[0][0])

