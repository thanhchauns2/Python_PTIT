n = int(input())
m = list(map(float,input().split()))
tmp = []
for i in m:
    if(i != min(m) and i!= max(m)):
        tmp.append(i)
print("%.2f" % float(sum(tmp)/len(tmp)))
