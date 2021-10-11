s = input()
c = sum(1 for c in s if c == '4' or c == '7')
if(c == 4 or  c == 7):
    print("YES")
else:
    print("NO")
