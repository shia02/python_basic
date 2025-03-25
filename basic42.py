#カプセル化

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        print('getter name')
        return self.__name
    
    def get_age(self):
        print('getter age')
        return self.__age
    
    def set_name(self, name):
        print('setter name')
        self.__name = name

    def set_age(self, age):
        print('setter age')
        self.__age = age

    name = property(get_name, set_name) #nameを呼び出すとset,getが呼ばれる
    age = property(get_age, set_age)

human = Human('taro', 20)
human.name = 'Jiro'
print(human.name)
human.age = 19