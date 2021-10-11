a = input()
tmp = ''.join(a.split('688'))
tmp = ''.join(tmp.split('68'))
tmp = ''.join(tmp.split('6'))
if(len(tmp) == 0):
    print('YES')
else:
    print('NO')
