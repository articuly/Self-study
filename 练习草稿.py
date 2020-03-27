s = 0
for i in range(1, 101):
    s += i
    if i == 50:
        print(s)
        break
else:
    print(1)


def area(l, w):
    return l * w


from datetime import timedelta, datetime


def timeplus(s):
    sometime = datetime.strptime(s, '%H:%M:%S')
    return sometime + timedelta(minutes=5, seconds=30)


result = timeplus('21:35:40')
print(result)


def fibona(n):
    a, b = 1, 2
    i = 1
    result = []
    while a <= n:
        result.append(a)
        a, b = b, a + b
        i += 1
    return result


print(fibona(40000))
print(len(fibona(40000)))

dicta = {"a": 1, "b": 2, "c": 3, "d": 4, "f": "hello"}
dictb = {"b": 3, "d": 5, "e": 7, "m": 9, "k": "world"}
dictc = dict()

for x, y in dicta.items():
    if x in dictb:
        dictc[x] = y + dictb[x]
    else:
        dictc[x] = y

for k, v in dictb.items():
    if k in dicta:
        dictc[k] = v + dicta[k]
    else:
        dictc[k] = v

print(dictc)
