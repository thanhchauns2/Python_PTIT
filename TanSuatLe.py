def solve():
    t = int(input());
    while t!=0:
        n = int(input())
        lst = input().split()
        lst = [int(i) for i in lst]
        m = [0] *1000001
        for i in range(0,n):
            m[lst[i]]+=1
        for i in range(0,n):
            if m[lst[i]]%2!=0:
                print(lst[i])
                break

        t-=1

if __name__ == "__main__":
    solve()
