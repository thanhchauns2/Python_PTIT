from math import sqrt; from itertools import count, islice

def snt(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def main():
    a = input().strip().split(' ')
    x = int(a[0]) 
    y = int(a[1]) 
    arr = []
    for i in range(x):
        a = list(map(int,input().split()))
        tmp = []
        for j in range(y):
            if(snt(int(a[j])) == True):
                tmp.append(1)
            else:
                tmp.append(0)
        arr.append(tmp)
    for i in range(x):
        for j in range(y):
            print(str(arr[i][j]), end =' ')
        print()

if __name__ == "__main__":
    main()
