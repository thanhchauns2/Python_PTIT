n = int(input())
for i in range(n):
    a = input()
    b = input()
    f = True
    if len(a) == len(b):
        for j in a:
            if(b.count(j) != a.count(j)):
                f = False
    else:
         f = False
    print("Test " + str(i + 1) +": " + ("YES" if f else "NO"))
