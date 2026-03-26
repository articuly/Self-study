from multipledispatch import dispatch


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

    @dispatch()
    def get_info(self):
        return print(f'getting student information')

    @dispatch(int)
    def get_info(self, value):
        return print(f'the student age is {value}')

    @dispatch(str)
    def get_info(self, value):
        return print(f'the student name is {value}')

    @dispatch(float)
    def get_info(self, value):
        if round(value) > value:
            return print(f'the student age is almost {round(value)}')
        else:
            return print(f'the student age is about {round(value)}')

    @dispatch(list)
    def study_class(self, value):
        for i in value:
            print(f'{self.name} is studying {i}')

    @dispatch(str)
    def study_class(self, value):
        print(f'{self.name} majors in {value}')


if __name__ == '__main__':
    s = Student('tom', 20)
    print(s)
    s.get_info()
    s.get_info('tom')
    s.get_info(20)
    s.get_info(20.6)
    s.study_class('business administrate')
    s.study_class(['math', 'chinese', 'english', 'art'])
