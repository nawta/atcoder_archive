n=int(input())
t,a=list(map(int,input().split()))
h=list(map(int,input().split()))
imin=100000
suf=0
for i in range(n):
  h[i]=t- h[i]*0.006
  if a>=h[i]:
    if imin>a-h[i]:
      #print("!!",a-h[i],h[i],i)
      imin=abs(a- h[i])
      suf=i
  else:
    if imin>h[i]-a:
      #print("!!",a-h[i],h[i],i)
      imin=abs( h[i]-a)
      suf=i 
print(suf+1)