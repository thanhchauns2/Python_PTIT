from math import sqrt; from itertools import count, islice; import sys; import array as arr
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
m = list(map(int,input().split()))
tmp = list(filter(lambda x : snt(x),m))
while(len(tmp) > 0):
    a = tmp[0]
    c = 0
    while(tmp.count(a) > 0):
        tmp.remove(a)
        c += 1
    print(str(a) +' ' + str(c))   
