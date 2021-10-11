n = int(input())
for i in range(n):
    m = input()
    s = 0
    mul = 1
    for i in range(len(m)):
        if(int(m[i]) != 0):
            if(i & 1):
                mul *= int(m[i])
            else:
                s += int(m[i])
    if(int(m[1::2]) == 0): mul = 0
    print(str(s) + ' ' + str(mul))
