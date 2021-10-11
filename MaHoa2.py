P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    inp = input()
    if(inp == '0'): break;
    a = inp.split(' ')
    tmp = a[1][::-1]
    for i in tmp:
        print(P[(P.find(i) + int(a[0])) % 28],end ='')
    print()
