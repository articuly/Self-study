a = 12
b = 30
if b > a:
    print("hello")
if b < 31:
    print("you are ritht")
age = int(input("请输入你的年龄："))
print(type(age))
print(age)
if age < 21:
    print("你不能吸烟")
elif age == 21:
    print("你快可以吸烟了")
elif age > 60:
    print("你很老了，请不要再吸烟了！")
elif 21 < age <= 60:
    print("你可以吸烟")
else:
    print("输入有误")
