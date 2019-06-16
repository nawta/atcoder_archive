n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
warm = 0
count = 0
rear = 0
for i in range(n):
    warm += a[i]
    while warm >= k:
        count += n - i
        warm -= a[rear]
        rear +=1
print(count)