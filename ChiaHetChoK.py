s = input().split(' ')
res = []
n = 0
while(True):
    n += 1
    if(int(s[1]) * n > int(s[2])): 
        break
    if(int(s[1]) * n - int(s[0]) > 0):
        res.append(int(s[1]) * n - int(s[0]))

if(len(res) == 0):
    print(-1)
else:
    for i in res :
        print(i,end=' ')
print()
