a,b,c,k=list(map(int, input().split()))
s,t=list(map(int, input().split()))
print(a*s + b*t -(s+t)*c*(s+t>=k))