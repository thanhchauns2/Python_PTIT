n = int(input())
for i in range (n):
    tmp = input()
    s = 0
    f = True
    for j in range(1,len(tmp),1):
        s += int(tmp[j])
        if(abs(int(tmp[j]) - int(tmp[j - 1])) != 2):
            f = False
            break
    if(f == True and ((s + int(tmp[0])) % 10 == 0)):
        print("YES")
    else:
        print("NO")
