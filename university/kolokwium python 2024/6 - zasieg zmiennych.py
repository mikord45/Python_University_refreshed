def local():
    x = 5
    print("x1: ", x)

local()
# print("x2: ", x)

def use_global():
    print(a)

a = 23
use_global()

import __main__
print(__main__.a)
print(__main__.use_global)

def use_enclosing():
    b = 5
    def inner():
        print(b)
    inner()

use_enclosing()

def use_enclosing():
    def f1():
        def f2(): print(x)
        x= 6
        f2()
        x = 5
    f1()
use_enclosing()

def make_adder(a):
    def f1(b):
        print(str(a) + str(b))
    return f1

c = make_adder('pies ')
c('i kot')

import builtins
print(builtins)
print(dir(builtins))
print(dir(__builtins__))

import keyword
print(keyword.kwlist)

a = 1
def f():
    a = 2
    print(a)
f()

a = 1
def f1():
    print(a)
    # a = 2
f1()

# l = []
# def f2():
#     l += [1,2]
# f2()

print(int)
int = 14
print(int)

def create_global():
    global x
    x =15

create_global()
print(x)

def modify_global():
    global y
    y = -y

y = 10
modify_global()
print(y)

z = 10
def f():
    z = 11
    def g():
        global z
        print(z)
    g()
f()

def make_counter():
    def increase():
        increase.count += 1
        print(increase.count)
    increase.count = 0
    return increase

counter = make_counter()
counter()
counter()
counter()
print(counter.count)