import math

def getSum(n):
        sum = 1
        while (n >0):
            sum *= n % 10
            n = n//10

        return sum

def solve():
    t=int(input())
    while t>0:
        n=int(input())
        a=[int(i) for i in input().split()]
        res = []
        for i in range(n):
            res.append([getSum(a[i]),a[i]])
        res.sort()
        x=""
        for i in range(len(res)):
            x=x+str(res[i][1])+" "
        print(x)
        t-=1


if __name__ == "__main__":
    solve()
