n = int(input())
print(int(n/1.08) if int(n/1.08)*1.08 == n else  (int(n/1.08)+1) if int((int(n/1.08)+1)*1.08)== n else ":(")