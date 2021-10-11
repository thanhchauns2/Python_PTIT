n = input()
if(len(n) % 3 != 0):
    n = "0"*((3 * (len(n)// 3 + 1)) - len(n)) + n
i = 0
tmp = []
kq = []
while i < len(n):
    tmp.append(n[i:i + 3:])
    i += 3
for i in tmp:
    t = 0
    i = i[::-1]
    for j in range(len(i)):
        t += 2 ** int(j) * int(i[j])
    kq.append(t)
print("".join(map(str,kq)))
