def dem(s):
	sum = 0
	count = 0
	while (len(s) > 1):
		sum = 0
		for i in range(len(s)):
			sum += (ord(s[ i ]) - ord('0'))
		s = str(sum)
		count += 1
	return count

s = input()
print(dem(s))
