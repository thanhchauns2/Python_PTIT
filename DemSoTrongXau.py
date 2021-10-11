n = int(input())
for i in range(n):
    a = input()
    b = input()
    c = 0
    while(a.find(b) != -1):
        a = a[a.find(b)+len(b)::]
        c += 1
    print(c)

            
    
