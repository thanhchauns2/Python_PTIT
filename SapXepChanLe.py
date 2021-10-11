n = int(input())
m = []
while True:
    tmp = list(map(int,input().split()))
    for i in tmp:
        m.append(i)
    if(len(m) == n): break
even = sorted(list(filter(lambda x: x % 2 == 0,m)))
odd = sorted(list(filter(lambda x : x & 1,m)),reverse = True)
x = 0
y = 0
lst = []
for i in m:
    if(i & 1):
        lst.append(odd[y])
        y -=-1
    else:
        lst.append(even[x])
        x +=1
for i in lst:
    print(i,end = ' ')
            
    
