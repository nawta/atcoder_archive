s = input()
t = s.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")
print("YES" if len(t) == 0 else "NO")