def findCommon(res,ar1, ar2, ar3, n1, n2, n3):
	i, j, k = 0, 0, 0
	while (i < n1 and j < n2 and k< n3):
		if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
			res.append(ar1[i])
			i += 1
			j += 1
			k += 1
		elif ar1[i] < ar2[j]:
			i += 1
		elif ar2[j] < ar3[k]:
			j += 1
		else:
			k += 1

t=int(input())
while t>0:
    n1n2n3=[int(i) for i in input().split()]
    n1=n1n2n3[0]
    n2=n1n2n3[1]
    n3=n1n2n3[2]

    ar1 = [int(i) for i in input().split()]
    ar2 = [int(i) for i in input().split()]
    ar3 = [int(i) for i in input().split()]

    res = []
    findCommon(res,ar1, ar2, ar3, n1, n2, n3)
    if(len(res)==0): print("NO")
    else:
        for i in res:
            print(i, end=" ")
    print()
    t-=1
