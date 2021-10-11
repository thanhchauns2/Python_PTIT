n = int(input())
for i in range(n):
    flag = True
    tmp = input()
    for i in range(1,len(tmp),1):
        if(int(tmp[i - 1]) > int(tmp[i])):
            print("NO")
            flag = False
            break
    if(flag == True):
        print("YES")
