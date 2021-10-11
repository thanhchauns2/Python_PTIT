from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
for i in range (n):
    m = input()
    a = int(m[-3::])
    b = int(m[:3:])
    if(snt(a) and snt(b)):
        print("YES")
    else:
        print("NO")



       
