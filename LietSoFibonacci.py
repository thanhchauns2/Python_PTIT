def mul_metrix_1(m1, m2):
    return (
        m1[0][0] * m2[0] + m1[0][1] * m2[1],
        m1[1][0] * m2[0] + m1[1][1] * m2[1]
    )


def mul_matrix(m1, m2):
    return (
        (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]),
        (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1])
    )


def pow_matrix(m, n):
    if n == 1:
        return m
    elif n % 2 == 0:
        a = pow_matrix(m, n / 2)
        return mul_matrix(a, a)
    else:
        return mul_matrix(pow_matrix(m, n - 1), m)


def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    a = ((1, 1), (1, 0))
    an = pow_matrix(a, n)
    pair_0 = (1, 1)
    pair_n = mul_metrix_1(an, pair_0)
    return pair_n[1]

c = int(input())
for i in range(c):
    tmp = input().split(' ')
    for j in range(int(tmp[0]) - 1,int(tmp[1]),1):
        print(fibo(j),end=' ')
    print()
