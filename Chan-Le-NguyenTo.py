from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
for i in range (n):
    tmp = input()
    s = 0
    f = True
    for j in range(len(tmp)):
        s += int(tmp[j])
        if(not((j + int(tmp[j])) % 2 == 0)):
            f = False
            break
    if(f == True and snt(s)):
        print("YES")
    else:
        print("NO")
