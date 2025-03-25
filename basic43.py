#カプセル化、一般的なやり方

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('getter name')
        return self.__name
    
    @property
    def age(self):
        print('getter age')
        return self.__age
    
    @name.setter
    def name(self, value):
        print('setter name')
        self.__name = value

    @age.setter
    def age(self, age):
        print('setter age')
        if age < 0:
            print('0以上を設定してください')
            return
        self.__age = age

human = Human('taro', -1)
human.name = 'Jiro'
print(human.age)
human.age = 12