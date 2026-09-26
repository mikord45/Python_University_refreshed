a = 78
print(type(a))

a = 'abc'
print(type(a))

a = {}
b = {}
c = b
print(id(a))
print(id(b))
print(id(c))
print(a == b)
print(b == c)
print(a == c)
print(a is b)
print(b is c)
print(a is c)

a[34] = 'x'
b[35] = 'y'
c[36] = 'z'
print(a, b, c)

l1 = []
l2 = l1
l1 += [1,2,3]
l2 += [4,5,6]
print(l1, l2)

s1 = ''
s2 = s1
print(id(s1))
print(id(s2))
s1 += '123'
s2 += '456'
print(s1)
print(s2)
print(id(s1))
print(id(s2))

print("----")
a = [1,2,3]
b = a[:]
print(b)
del b[1]
print(a)
print(b)

d1 = {'a': [1,2,3]}
d2 = d1.copy()
d2['a'].append(4)
print(d1)
print(d2)

import copy
d3 = copy.deepcopy(d1)
d3['a'].append(5)
print(d1)
print(d2)
print(d3)

a = [1,2]
a.append(a)
print(a)
print(a is a[2])
print(a[2] is a)
print(a[2][2][2])

print(isinstance(1, int))
print(isinstance(1, str))
print(isinstance(True, bool))
print(isinstance(True, int))

napis = '7 skrzyń fig'
stats = {'cyfry': 0, 'litery': 0, 'spacje': 0}
for litera in napis:
    if(litera.isdigit()):
        stats.update({'cyfry': stats.get('cyfry') + 1})
    elif(litera.isalpha()):
        stats.update({'litery': stats.get('litery') + 1})
    elif(litera.isspace()):
        stats.update({'spacje': stats.get('spacje') + 1})
print(stats)
