n = input()
k = int(input())
if(len(n) & 1): n = n[:len(n) - 1:]
i = 0
tmp = []
while i < len(n):
    tmp.append(int(n[i:i + 2:]))
    i += 2
ans = sorted(set(tmp))
c = 0
for i in ans:
    if(tmp.count(i) >= k):
        print(str(i) + ' ' + str(tmp.count(i)))  
    else :
        c += 1
if(c == len(ans)): print("NOT FOUND")
