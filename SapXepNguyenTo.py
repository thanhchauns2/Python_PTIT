from math import sqrt, gcd; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


a = input()
b = list(map(int,input().split()))
s = list(filter(lambda x : snt(x),b))
tmp = sorted(s)
c = 0
d = []
for i in b:
    if(snt(i)):
        d.append(tmp[c])
        c += 1
    else:
        d.append(i)
for i in d:
    print(i, end= ' ')


            
    
