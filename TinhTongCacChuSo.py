import re
n = int(input())
for i in range(n):
    _ = input()
    tmp1 = re.sub(r'[0-9]','',_)
    tmp2 = re.findall(r'\d',_)
    total = 0
    for i in tmp2:
        total += int(i)
    res = "".join(sorted(tmp1))
    print(res + str(total))
