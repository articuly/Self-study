# *args 参数, as a tuple
def add(*args):
    print(sum(args))


def abc(*arts):
    for n in arts:
        print("number is", n)


add(1, 2, 3, 4, 5, 6, 7)
abc(12, 23, 34, 45)
