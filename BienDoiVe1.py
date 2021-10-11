def process(n):
    if(n == 1): return 1
    elif(int(n) & 1): return process(n * 3 + 1) + 1
    else: return process(n/2) + 1

while True:
    a = int(input())
    if(a == 0): break
    print(process(a))
