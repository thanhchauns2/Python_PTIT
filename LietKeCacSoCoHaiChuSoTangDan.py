n = input()
if(len(n) & 1): n = n[:len(n) - 1:]
i = 0
tmp = []
while i < len(n):
    tmp.append(int(n[i:i + 2:]))
    i += 2
ans = sorted(set(tmp))
for i in ans:
    print(i, end = ' ')
print()
