n = int(input())
for i in range(n):    
    s = input()
    c = sum(1 for c in s if c == '4' or c == '7')
    if(c == len(s)):
        print("YES")
    else:
        print("NO")
