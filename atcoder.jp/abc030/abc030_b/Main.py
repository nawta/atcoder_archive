n, m = map(int, input().split())
n = n % 12
N = 30 * (n + m / 60) 
M = 6 * m  
x = abs(N - M)
print(min(x, 360 - x))
