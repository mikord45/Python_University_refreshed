from fractions import Fraction

a = Fraction(1,3) + Fraction(4,5)
print(a)

# b = (2.3).as_integer_ratio()
# print(b)
b = Fraction(2.3)
b = b.limit_denominator(10 ** 14)
print(b)
c = b + 0.2
print(c)

import decimal
print(0.2 + 0.1)
print(decimal.Decimal('0.2') + decimal.Decimal('0.1'))
print(decimal.Decimal('0.1'))
print(decimal.Decimal(0.1))
print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal('1')/decimal.Decimal('3'))
print(decimal.Decimal('1')/3)
decimal.getcontext().prec = 2
print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal('1')/decimal.Decimal('3'))
print(decimal.Decimal('1')/3)

print(complex('1+2j'))
print(2j)
print(1+2j)
x = complex('1+2j')
print(x.real)
print(x.imag)

d = float('inf')
print(d)
print(5 + d)
e = float('nan')
print(e)
print(d + e)
f = float('-inf')
g = float('inf')
print(f + g)

h = divmod(10,3)
print(h)

i = decimal.Decimal('2.6')
j = i.as_integer_ratio()
print(j)