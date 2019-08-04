s = input()
n = len(s)

succession = 1
max_succession = 0

anal = [0]*n
l_tmp = 1
judge = 1

for i in range(1,n):
    if s[i] == "R":
        if s[i-1] == "R":
            succession += 1
            if  max_succession < succession:
                max_succession = succession
        else:
            anal[l_tmp] = succession
            succession = 1
    else:
        if s[i-1] == "L":
            succession += 1
            if  max_succession < succession:
                max_succession = succession
        else:
            anal[i-1] = succession
            succession = 1
            l_tmp = i
anal[l_tmp] = succession
#print(anal,l_tmp)

for i in range(n-1):
    if judge == 0:
        judge = 1
        continue
    else:
        if anal[i] != 0:
            if abs(anal[i+1] - anal[i]) >= 1:
                if max(anal[i+1],anal[i]) % 2 != 0:
                    if anal[i+1] > anal[i]:
                        tmp = (anal[i+1]+anal[i])
                        anal[i+1] = tmp // 2 + tmp%2
                        anal[i] = tmp // 2
                    else:
                        tmp = (anal[i+1]+anal[i])
                        anal[i+1] = tmp // 2
                        anal[i] = tmp //2 + tmp%2
                else:
                    if anal[i+1] > anal[i]:
                        tmp = (anal[i+1]+anal[i])
                        anal[i+1] = tmp // 2 
                        anal[i] = tmp // 2 + tmp%2
                    else:
                        tmp = (anal[i+1]+anal[i])
                        anal[i+1] = tmp // 2 + tmp%2
                        anal[i] = tmp //2 
                        
            judge = 0
            
for i in range(n):
    print(anal[i],end=" ")
print()