from math import sqrt; from itertools import count, islice

def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = input().split(' ')
s = []
a = 2
b = int(n[0])
c = int(n[1])
while(b > 0):
    if(snt(a) == True):
        s.append(a)
        b -= 1
    a += 1
print(c, end = ' ')
for i in s:
    print(c + i, end = ' ')
    c += i
print()
