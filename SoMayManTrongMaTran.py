n = list(map(int,input().split()))
a = []
biggest = 0
smallest = 10000000
for i in range(n[0]):
    tmp = list(map(int,input().split()))
    biggest = max(max(tmp),biggest)
    smallest = min(min(tmp),smallest)
    a.append(tmp)
c = 0
for i in a:
    c += len(list(filter(lambda x : x == (biggest - smallest),i)))
if(c != 0):
    print(biggest - smallest)
    for i in range(n[0]):
        for j in range(n[1]):
            if(a[i][j] == biggest - smallest):
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
else: print("NOT FOUND")
