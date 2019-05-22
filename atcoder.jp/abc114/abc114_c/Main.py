n = int(input())
sevenfivethree = []
judge = 0

def dfs(num: str):
    if int(num) > n or len(num) > 8:
        return
    else:
        if int(num+"3") <= n:
            sevenfivethree.append(num + "3")
        if int(num+"5") <= n:
            sevenfivethree.append(num + "5")
        if int(num+"7") <= n:
            sevenfivethree.append(num + "7")

        dfs(num + "3")
        dfs(num + "5")
        dfs(num + "7")

        return

dfs("3")
dfs("5")
dfs("7")

for i in range(len(sevenfivethree)):
    if sevenfivethree[i].count("3") ==0 or sevenfivethree[i].count("5") ==0 or sevenfivethree[i].count("7") ==0:
        sevenfivethree[i] = 0 #条件に合わないやつを0に書き換え
        judge = 1
print(len(set(sevenfivethree)) - (judge == 1)) #0があれば、setの数が1こ余分なので引く。
