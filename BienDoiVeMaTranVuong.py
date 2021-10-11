a = list(map(int,input().split()))
m = []
for i in range(a[0]):
    tmp = list(map(int,input().split()))
    m.append(tmp)
odd = []
even = []
x = 0; y = 1
if(a[0] > a[1]):
    for i in range(a[0] - a[1]):
        odd.append(x)
        x += 2
    for i in range(len(m)):
        if i not in odd:
            for j in range(len(m[i])):
                print(m[i][j], end = ' ')
        print()
elif(a[1] > a[0]):
    for i in range(a[1] - a[0]):
        even.append(y)
        y += 2
    for i in range(len(m)):
        for j in range(len(m[i])):
            if j not in even:
                print(m[i][j], end = ' ')
        print()
else:
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = ' ')
        print()
