n = int(input())
for i in range(n):
    m = int(input())
    beg = 2
    if(m & 1): beg = 1
    s = 0
    for i in range(beg,m + 1,2):
        s += 1/i
    print("%.6f" % float(s))
    
