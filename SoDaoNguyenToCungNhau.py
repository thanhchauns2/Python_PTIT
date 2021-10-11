from math import gcd
n = int(input())
for i in range(n):
    m = input()
    if(gcd(int(m),int(''.join(reversed(m)))) == 1):
        print("YES")
    else:
        print("NO")



       
