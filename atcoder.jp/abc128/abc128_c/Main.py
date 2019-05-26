numofswitch,numoflump = list(map(int, input().split()))
s = []
for i in range(numoflump):
    tmps = list(map(int, input().split()))
    s.append(tmps)
p = list(map(int, input().split()))
switch_counter = 0
num_of_comnination = 0

#print(s)
#print(p)

for switchcombi in range(2**numofswitch):
    Anal = 0
    for lumpindex in range(numoflump):
        switch_counter = 0
        for switch_checker in range(1,len(s[lumpindex])):
            if (switchcombi >> (s[lumpindex][switch_checker] -1)) % 2 == 1:
                #print("not Anal",switchcombi,lumpindex,switch_checker,s[lumpindex][switch_checker])
                switch_counter += 1
            #print("yaba poji",switchcombi,lumpindex,switch_checker,s[lumpindex][switch_checker])
        if switch_counter % 2 != p[lumpindex]:
            Anal = 1
            #print("Anal",switchcombi,lumpindex,switch_checker,s[lumpindex][switch_checker])
            break
    if Anal == 0:
        num_of_comnination += 1
print(num_of_comnination)