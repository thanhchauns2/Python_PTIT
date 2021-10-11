n = int(input())
for i in range(n):
    s = input()
    tmp1 = int(s[:2:])
    tmp2 = int(s[-2::])
    if(tmp1 == tmp2): print("YES")
    else: print("NO")
