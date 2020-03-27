class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return str(self.name)

    def get_age(self):
        return int(self.age)

    def get_course(self):
        return int(max(self.score))


zm = Student('zhangming', 20, [69, 88, 100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())


class People:
    name = 'Tom'
    age = 18

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def speak(self):
        print(f'{self.name} is speaking: I am {self.age} year old')


p = People('Sunny', 20)
print(People.name)
p.name = 'Jason'
p.speak()
