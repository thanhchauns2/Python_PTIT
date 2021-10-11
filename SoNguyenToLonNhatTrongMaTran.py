from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = list(map(int,input().split()))
a = []
biggest = 0
for i in range(n[0]):
    tmp = list(map(int,input().split()))
    t  = 0 if len(list(filter(lambda x: snt(x),tmp))) == 0 else max(list(filter(lambda x: snt(x),tmp)))
    biggest = max(t,biggest)
    a.append(tmp)
if(biggest != 0):
    print(biggest)
    for i in range(n[0]):
        for j in range(n[1]):
            if(a[i][j] == biggest):
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
else: print("NOT FOUND")



