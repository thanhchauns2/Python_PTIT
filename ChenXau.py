def solve():
    n = input()
    m = input()
    k =int(input())
    k-=1
    print(n[:k]+m+n[k:])

if __name__ == "__main__":
    solve()
