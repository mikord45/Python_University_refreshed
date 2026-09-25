import random
list2 = [(a, b) for a in range(0,10) for b in [random.randint(0,10)]]
print(list2)

sorted_list = sorted(list2, key=lambda t: t[1])
print(sorted_list)

lambda_function = lambda a, b, c: a*b*c
print(lambda_function(2,4,6))

print((lambda a, b, c: a+b+c)(3,6,9))

l = [5,10,15,20]
l2 = list(map(lambda x: x*2, l))
print(l2)

def multiply(x):
    return x*2
l3 = list(map(multiply, l))
print(l3)