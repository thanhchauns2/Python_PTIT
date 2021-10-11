from math import sqrt, gcd; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    if b.count(i) == 0:
        b.append(i)
i = 0
while(i <= len(b)):
    if(snt(sum(b[:i + 1:])) and snt(sum(b[i + 1::]))):
        print(i)
        break
    i += 1
if(i == len(b) + 1):
    print("NOT FOUND")
