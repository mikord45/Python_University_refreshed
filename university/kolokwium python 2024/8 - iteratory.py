# l = [1]
# for i in l: l.append(1)

l = [1,2,3]
i, j = iter(l), iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(j))
print(next(j))
print(next(j))
