from math import sqrt, gcd; from itertools import count, islice
def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
n = int(input())
for i in range(n):
    s = input().split(' ')
    a = str(gcd(int(s[0]), int(s[1])))
    t = 0
    for i in a:
        t += int(i)
    if(snt(t)):
        print("YES")
    else:
        print("NO")
