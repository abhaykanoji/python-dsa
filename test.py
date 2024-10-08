a = [i**2 if i%3==0 else i**3 for i in range(10)]
print(a)


b = {i:i**2 for i in range(5) }
print(b)


c = {i:i**2 if i%2==0 else i**3 for i in range(10) }
print(c)


lst = [1,2,2,3,3,3,4,4,4,4]

dict = {i:lst.count(i) for i in lst }
print(dict)
