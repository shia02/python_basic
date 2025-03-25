#クラスの継承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'hello {self.name}')

    def say_age(self):
        print(f'{self.age} year old')

class Employee(Person):
    def __init__(self, name, age, number):
        super().__init__(name,age)
        self.number = number

    def say_number(self):
        print(f'my number is {self.number}')

    def greeting(self):
        super().greeting()
        print('employee hello')

man = Employee('taro', 54, '020')
man.greeting()
man.say_age()
man.say_number()