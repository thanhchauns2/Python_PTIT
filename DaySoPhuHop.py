n = int(input())
for i in range (n):
    m = int(input())
    a = input().strip().split(' ')
    b = input().strip().split(' ')
    f = True
    c = sorted(map(lambda x: int(x),a))
    d = sorted(map(lambda x: int(x),b))
    for i in range(m):
        if(c[i] > d[i]):
            f = False
            break
    if(f == True) : print("YES")
    else: print("NO")
