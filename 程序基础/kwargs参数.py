# kwargs=keyword args, as a dictionary
def m1(*args, **kwargs):
    print(type(args))
    print(type(kwargs))


m1()

p1 = {'job': '星象占卜人員', 'company': '碩華電腦', 'ssn': 'L468819736', 'residence': '456 新營永安巷775號8樓', 'blood_group': 'A-',
      'website': ['http://shi.tw/'], 'username': 'zshen', 'name': '包承翰', 'sex': 'F', 'address': '101 汐止芝山街66號6樓',
      'mail': 'xiefang@gmail.com'}


def m2(ss):
    for k, v in ss.items():
        print(k, ":", v)


m2(p1)
