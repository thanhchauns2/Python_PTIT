import string
s = input()
if(int(len(s)/2) < sum(1 for c in s if c.isupper())):
    print(s.upper())
else:
    print(s.lower())
