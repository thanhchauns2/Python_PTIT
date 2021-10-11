n = int(input())
m = input().split(' ')
dem = 0
for i in range(1,len(m)):
    if(m[i - 1] != m[i]): dem += 1
print(dem)

       
