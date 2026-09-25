class Callable:
    def __init__(self):
        self.count = 0
        self.limit = 10

    def __call__(self, arg):
        print(str(arg) + ' from call')

    def __repr__(self):
        return 'custom repr'

    def  __str__(self):
        return 'custom str'

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if (self.count > self.limit):
            raise StopIteration
        return self.count ** 2

    def __add__(self, other):
        return 5

    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return False

    def __sub__(self, other):
        return 0

    def __mul__(self, other):
        return 100

    def __truediv__(self, other):
        return -100

    def __iadd__(self, other):
        return 500

c = Callable()
c('arg1')
print(repr(c))
print(str(c))
for x in c:
    print(x)

c2 = Callable()
print(c + c2)
print(c - c2)
print(c * c2)
print(c / c2)
c += 100
print(c)