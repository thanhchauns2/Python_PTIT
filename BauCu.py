n = list(map(int,input().split()))
a = list(map(int,input().split()))
t = set(a)
t = sorted(t,key = lambda x : a.count(x), reverse = True)
c = 0
if(len(t) == len(list(filter(lambda x : a.count(x) == a.count(t[0]),t)))):
    print("NONE")
else:
    for i in t:
        if a.count(i) < a.count(t[0]):
            c = a.count(i)
            break
    tmp = sorted(list(filter(lambda x : a.count(x) == c, t)))
    print(tmp[0])
