from abc import abstractmethod, ABCMeta

class Animals(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animals):
    def speak(self):
        print('わん')

class Cat(Animals):
    def speak(self):
        print('にゃー')

class Sheep(Animals):
    def speak(self):
        print('めー')

class Other(Animals):
    def speak(self):
        print('そんな動物はいない')


val = input('1,2,3のうちどれかを入力してください\n')
if val == '1':
    animal = Dog()
elif val == '2':
    animal = Cat()
elif val == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak()