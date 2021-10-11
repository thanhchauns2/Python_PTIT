def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve():
    a = [int(i) for i in input().split()]
    n = a[0]
    k = a[1]
    cnt = 0
    for i in range(10**(k-1), 10**(k)):
        if gcd(n, i) == 1:
            cnt += 1
            print(i, end=" ")
            if cnt == 10:
                print()
                cnt = 0


if __name__ == "__main__":
    solve()
