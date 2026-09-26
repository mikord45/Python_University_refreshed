s1 = set('zdanie z literami')
print(s1)
s2 = set([1, 68, 66, 66])
print(s2)
s3 = {6, 5, 5}
print(s3)

print(6 in s3)
print(4 in s3)
print(list(s3))
print(len(s3))

s4 = {2,5,7,3,5,11,45}
print(s4)
s4.add(4)
s4.remove(5)
print(s4)
# s4.add(4)
# print(s4)
# s4.remove(10)
# print(s4)
s4.update(['test1','test2'])
print(s4)
s4.update('kot')
print(s4)

print('=======')

s1 = set('abc')
s2 = set('acf')
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
s3 = s1 | s2
print(s3)
s1 |= s2
print(s1)
print(s1 >= s2)
print(s1 <= s2)

print('=======')

s10 = set('abc')
s20 = set('xyz')

print(s10 - s20)

print('========')
# set([1,2,[3]])

s30 = set('kot')
print(s30)
s30f = frozenset('kot')
print(s30f)
s30.remove('k')
print(s30)
# s30f.remove('k')
print(s30f)
