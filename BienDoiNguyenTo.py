from math import sqrt; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


n = input()
a = list(map(int,input().split()))
m = 0
for i in a:
    step1 = 0; step2 = 0
    if not snt(i):
        while True:
            step1 += 1
            if(snt(i + step1)):
                break
        while True:
            step2 += 1
            if(snt(i - step2)):
                break
        m = m if m > min(step1,step2) else min(step1,step2)
print(m)
