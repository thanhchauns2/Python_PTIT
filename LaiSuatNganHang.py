n = int(input())
for i in range(n):
    m = list(map(float,input().split()))
    n = 1 
    while True:
        if(m[2] <= m[0]*(1 + m[1]/100)**n):
            print(n)
            break
        n += 1

