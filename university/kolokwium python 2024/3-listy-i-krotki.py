a = list('kot')
print(a)

b = range(20,90,5)
print(b)
c = list(b)
print(c)
print(len(c))

print(type([]))

d = c[3:7]
print(d)

print("====")

e = d + ['a', 'b'] * 3
print(e)
e[3:] = []
print(e)

e.append("test1")
print(e)
e.extend(["test2", "test3"])
print(e)
e.extend("test4")
print(e)
e.insert(2, 'test5')
print(e)
e.reverse()
print(e)

print("----")
del e[:3]
print(e)
e[4:] = []
print(e)
e.remove('test3')
print(e)
print(e.pop(1))
print(e)

print('test2' in e)
print(e.index('e'))

e.append("a")
print(e)
print(sorted(e))
print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)
e.sort()
print(e)
print(sorted(e, reverse=True))

print("=========")

f = 1,2,3
print(type(f))
g = (1,2,3)
print(type(g))
h = 1,
print(type(h))
i = (1,)
print(type(i))

print("=======")

var1, var2 = 1, 2
var1, var2 = var2, var1
print(var1)
print(var2)

j = 1,2,3,'kot'
print(j[3])
print(j[1:])
k = j * 3
print(k)

l = [1,2,3]
[la,lb,lc] = l
print(la)
print(lb)
print(lc)
(x, y, z) = l
print(type(x))
print(x)

t = 'x1', 'y2', 'z3'
t1, t2, t3 = [t10, t20, t30] = t
print(t10)
print(t2)