import math

multiline = """line1
line2
line3"""
print(multiline)

t1 = '\temp'
print(t1)
t2 = '\\temp'
print(t2)
t3 = r'\temp'
print(t3)

a = 'tekst testowy'
print(a[3])
print(a[5:])
print(a[:-3])
b = a[:]
print(b)
print(b[4::-3])
print(b[8:2:-2])
c="0123456789"
print(c[4:9:2])
print(c[9:4:-2])

print(a[:2] + a[3:8] + 'k' + a[8:])

d = "tekst"
d += ' nowy'
print(d)
d *= 2
print(d)

print(ord('a'))
print(chr(98))

s = 'ala ma kota'
print('ma' in s)
print(s.find('ma'))

s += "\n"
print(s)
s = s.rstrip()
print(s)
print("====")

s = s.upper()
print(s)
s = s.lower()
print(s)

print('*'.join(s.split()))
print(s.startswith('ala'))

city = "łódź"
print(city)

###########

source = "kraków"
print("======")
print(type(source))
print(source)

u = source.encode('utf8')
print(type(u))
print(u)
b = source.encode('iso-8859-2')
print(type(b))
print(b)
# result = source + u
result = source + u.decode('utf8')
print(result)

###########

val1 = 234
val2 = 'abc'
print(str(val1), repr(val1))
print(str(val2), repr(val2))

#######

r1 = 'test1'
r2 = 'test2'
print('first value %s, second value %s' % (r1, r2))

print('number value is %.2f' % math.pi)

n1 = 5
print('value = %10d' % n1)

print('{0} - {1} - {1} - {0}'.format('ala', 'kota'))
print('{0} - {1!r} - {1!s} - {0}'.format('ala', 'kota'))
