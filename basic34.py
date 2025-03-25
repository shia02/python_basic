#インスタンス、クラス、スタティックメソッド
class Human:
    class_name = 'Human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print('インスタンスメソッド')
        print(f'{self.name=} {self.age=}')

    @classmethod
    def print_class_name(cls, msg):
        print('クラスメソッド')
        print(cls.class_name)
        print(msg)

    @staticmethod
    def print_msg(msg):
        print('スタティックメソッド')
        print(msg)

Human.print_class_name('msg')
human = Human('tar0', '19')
human.print_name_age()
human.print_class_name('msg')
Human.print_msg('msg')
human.print_msg('msg')