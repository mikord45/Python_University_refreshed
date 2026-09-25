def square_gen():
    x = 1
    while True:
        yield x**2
        x += 1

s = square_gen()
print(s)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

def generator():
    while True:
        print('wykonałem pierwszą linię')
        yield 1
        print('wykonałem drugą linię')

g = generator()
print(next(g))
print('-----')
print(next(g))
print('-----')
print(next(g))
print('-----')
print(next(g))

def generator2():
    yield 2

g2 = generator2()
print(next(g2))
print("====")
# print(next(g2))

def range_gen(limit):
    i = 0
    while (i < limit):
        yield i
        i += 1

for x in range_gen(3):
    print(x)

print("======")
def test_generator():
    received1 = yield 1
    print(received1)
    received2 = yield 2
    print(received2)
    received3 = yield 3
    print(received3)
    received4 = yield 4
    print(received4)
    received5 = yield 5
    print(received5)
    received6 = yield 6
    print(received6)

test_g = test_generator()
print(next(test_g))
print(next(test_g))
print(next(test_g))
print(next(test_g))
print(test_g.send(50))
print(next(test_g))