from math import gcd
n = int(input())
tmp = list(map(int,input().split()))
tmp.sort()
for i in range(len(tmp) - 1):
    for j in range(i + 1, len(tmp),1):
        if(gcd(tmp[i],tmp[j]) == 1):
            print(str(tmp[i]) + ' ' + str(tmp[j]))
