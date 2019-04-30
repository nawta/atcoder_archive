n=int(input())
cityname_candidate=""
largest_population = 0
total_population = 0
for i in range(n):
    s,p=input().split()
    p = int(p)
    if p>largest_population:
        largest_population = p
        cityname_candidate = s
    total_population += p
print("atcoder" if total_population >= largest_population*2 else cityname_candidate)
