a = []
while(len(a) < 10):
    tmp = input().split(' ')
    for i in tmp:
        a.append(i)
c = []
for i in a:
    if(c.count(int(i) % 42) == 0):
        c.append(int(i) % 42)
print(len(c))
