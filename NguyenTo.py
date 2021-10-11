from math import sqrt,gcd; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
for i in range(n):
    tmp = int(input())
    k = 0
    for i in range(1,tmp,1):
        if(gcd(i,tmp) == 1):
            k += 1
    if(snt(k)):
        print("YES")
    else:
        print("NO")
