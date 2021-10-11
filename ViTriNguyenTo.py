from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
n = int(input())
for i in range(n):
    tmp = input()
    f = True
    for j in range(len(tmp)):
        if(snt(j) ^ snt(int(tmp[j]))):
            f = False
            break
    if(f == True): print("YES")
    else: print("NO")
       
