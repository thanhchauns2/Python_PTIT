def check_reverse(n):
    return len(str(n)) > 1 and n == int(str(n)[::-1])
n = list(map(int,input().split()))
a = []
biggest = 0
for i in range(n[0]):
    tmp = list(map(int,input().split()))
    t  = 0 if len(list(filter(lambda x: check_reverse(x),tmp))) == 0 else max(list(filter(lambda x: check_reverse(x),tmp)))
    biggest = max(t,biggest)
    a.append(tmp)
if(biggest != 0):
    print(biggest)
    for i in range(n[0]):
        for j in range(n[1]):
            if(a[i][j] == biggest):
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
else: print("NOT FOUND")
