n = int(input())
for i in range(n):
    tmp = input()
    f = True
    if len(tmp) & 1 and tmp[0] != tmp[1]:
        for i in range(2,len(tmp),2):
            if(tmp[i] != tmp[i-2]):
                f = False
    else:
        f = False
    if(f == True):
        print("YES")
    else:
        print("NO")
