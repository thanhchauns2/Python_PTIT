s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m = int(input())
for i in range(m):
    n = list(map(int,input().split()))
    tmp =""
    while n[0] != 0 :
        tmp += str(s[n[0] % n[1]])
        n[0] = n[0] // n[1]
    print(tmp[::-1])
