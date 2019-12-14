# initialize
class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def studlike(self):
        print(self.name, "can walk")
        print(self.name, "is", self.age)


s1 = Students("int", "12")
s1.studlike()
s2 = Students("art", "23")
s2.studlike()
