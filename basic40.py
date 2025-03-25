#ポリモーフィズム

from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    def say_something(self):
        print(f'女性{self.name=}')

class Man(Human):
    def say_something(self):
        print(f'男性{self.name=}')

num = input('0かその他を入力してください\n')
if num == '0':
    human = Man('taro')
else:
    human = Woman('hanako')

human.say_something()