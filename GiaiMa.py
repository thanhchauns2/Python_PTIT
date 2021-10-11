n = int(input())
for i in range(n):
    s = input()
    for i in range(int(len(s)/2)):
        tmp = s[2 * i: 2 * (i + 1)]
        print(tmp[0] * int(tmp[1]),end='')
    print()
    
    
