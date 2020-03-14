h,w = list(map(int, input().split()))

print((w//2)*h + (h//2 + (h%2 != 0))*(w % 2 != 0) if w != 1 and h != 1 else 1)