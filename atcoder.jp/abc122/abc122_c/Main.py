n,q=list(map(int, input().split()))
s=input()

t=[0]*n

s=s.replace("AC", "Ac")
#s=s.translate(str.maketrans({'AC':'aC'})) maketransは置換元一文字じゃないといけんみたい
for i in range(n):
  if s[i] == "c":
    if i !=0:
      t[i]=1+t[i-1]
    else:
      t[i]=1
  else:
    t[i]=t[i-1]

#print(t)
for _ in range(q):
  l,r=list(map(int, input().split()))
  print(t[r-1]-t[l-1])