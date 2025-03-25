#クラス
class Car:
    """車クラス"""
    country = 'Japan'
    year = 2019
    name = 'Prius'
    def print_name(self):
        print('print name 実行')
        print(self.name)

my_car = Car()
my_car.print_name()
list_a = ['apple', 'grape', Car]
second_car = list_a[2]()
second_car.print_name()
help(Car)