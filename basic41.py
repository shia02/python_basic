#プライベート変数

class Human:

    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_name(self):
        print(f'name = {self.__name}')

human = Human('taro', 20)
print(human._Human__name) #無理やりアクセスできる
human.print_name()