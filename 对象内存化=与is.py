from sys import intern

a = 'hello world'
b = 'hello world'
print(id(a), id(b))
print(a is b)

c = intern(a)
d = intern(b)
print(id(c), id(d))
print(c is d)

e = [1, 2, 3]
f = [1, 2, 3]
print(id(e), id(f))
print(e is f)

g = e
print(e is g)

h = e.copy()
print(id(e), id(g), id(h))
print(h is e)


class SillyStr(str):
    # this method gets called when using == on the object
    def __eq__(self, other):
        print(f'comparing {self} to {other}')
        return len(self) == len(other)


print('hello python' == 'hello python')
print('hello python' == SillyStr('hello python'))
print(SillyStr('hello') == [1, 2, 3, 4, 5])
