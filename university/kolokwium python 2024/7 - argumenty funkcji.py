def insert(collection, position, value):
    collection[position] = value
    collection = ['something',  'new']
    return collection
c = [1,8,23]
print(insert(c, 2, 80))

print(c)

args = [1, 2]
args.append(3)
print(args)

def print3(a, b, c):
    print(a, b, c)

print3(*args)
print3(*[1, 2, 3])
print3(*(1, 2, 3))
print3(*range(1, 4))
print3(1, *[2, 3])
print3(1, c=3, *[2])

def print4(a, b, c, d):
    print(a, b, c, d)

args = {
    "d": 4,
    "c": 3,
    "b": 2,
    "a": 1
}

print4(**args)
print4(1, *[2], **{'c': 3}, d=4)

def call2(function, args, args2):
    return function(*args, **args2)

print(call2(sorted, [[1,2,3,4,5]], {'reverse': True}))

def f1(key, value, a = {}):
    a[key] = value
    return a

print(f1(1,2))
print(f1(3,4))
print(f1(5,6))
print(f1(7,8, {}))
print(f1(9, 10))

def print_everything(*args, **args2):
    print(args)
    print(args2)
print_everything(1, e = 5, *[3, 4], **{'d': 6, 'f': 7})

def print_everything2(*args, a, b):
    print(a)
    print(b)
    print(*args)

print_everything2(543, 54353234, 234234, a=10, b=20)