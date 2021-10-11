a = input().split('=')
b = a[0].split('+')
tmp = int(b[0]) + int(b[1])
if(tmp == int(a[1])):
    print("YES")
else:
    print("NO")
