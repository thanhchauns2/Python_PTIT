n = input()
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
tmp =[]
A = sorted(set(a))
B = sorted(set(b))
for i in A:
    if i in B:
        print(i,end= ' ')
print()
for i in A:
    if i not in B:
        print(i,end= ' ')
print()
for i in B:
    if i not in A:
        print(i,end= ' ')
print()
