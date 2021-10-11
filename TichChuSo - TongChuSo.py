n = int(input())
for i in range(n):
    m = input()
    s = 0
    mul = 1
    for i in range(len(m)):
        if(int(m[i]) != 0):
            if(i & 1):
                s += int(m[i])
            else:
                mul *= int(m[i])
    print(str(mul) + ' ' + str(s))
