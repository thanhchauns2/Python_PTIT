n = int(input())
for i in range(n):    
    s = input()
    t = 0
    for i in s:
        t += int(i)
    if(t % 3 == 0):
        print("YES")
    else:
        print("NO")
