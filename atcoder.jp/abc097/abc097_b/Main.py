import sys
import math

def isExponential(i : int) -> bool:
    for j in range(2,math.ceil(math.sqrt(i))+1):       
        devidend = i
        devisor = j
        #print(devidend,devisor,"inFor") 
        while 1:
            #print(devidend,devisor,"inWhile")
            if devidend % devisor != 0:
                break
            else:
                if devidend == devisor:
                    return True
                else:
                    devidend //= devisor
    return False

x = int(input())
if x == 1:
    print(1)
for i in range(x,0,-1):
    if isExponential(i) == True:
        print(i)
        #print("wtf")
        break