from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
for i in range (n):
    m = input()
    dem = 0
    for i in m:
        if(snt(int(i))):
            dem += 1
    if(snt(len(m)) and dem > len(m) - dem):
        print("YES")
    else:
        print("NO")




       
