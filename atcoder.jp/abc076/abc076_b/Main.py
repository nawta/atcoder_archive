n = int(input())
k = int(input())
number = 1
for i in range(n):
    number = min(number+k, number*2)
print(number)