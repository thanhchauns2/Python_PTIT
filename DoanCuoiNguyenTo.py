from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
for i in range (n):
    m = int(input()[-4::])
    if(snt(m)):
        print("YES")
    else:
        print("NO")



       
