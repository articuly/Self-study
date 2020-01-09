class student():
    place = "home"

    def eat(self, name, age):
        print(name, "can eat,"+" and he is ", age)

    def cook(self):
        print("student may cook at", self.place)

    def study(self, name):
        print(name + " can study.")

    @staticmethod
    def walk():
        print("student can walk.")


student().eat("art", "18")
student().cook()
student().study("abc")
student().walk()
