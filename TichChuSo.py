n = int(input())
for i in range(n):    
    s = input()
    t = 1
    for i in s :
        if(i == '0'): continue
        t *= int(i)
    print(t)
