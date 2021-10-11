n = int(input())
for i in range(n):
    m = input()
    t = 0
    for j in m:
        t += int(j)
    if(t == int(str(t)[::-1]) and t >= 10):
        print("YES")
    else:
        print("NO")
