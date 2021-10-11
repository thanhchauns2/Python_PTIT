while(True):
    n = int(input())
    if(n == 0): break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    if(min(arr) != max(arr)):
        print(str(min(arr)) + " " + str(max(arr)))
    else:
        print("BANG NHAU")
