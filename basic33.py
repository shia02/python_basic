#コンストラクタ
class SampleClass:
    def __init__(self, msg, name=None):
        print('コンストラクタ起動')
        self.msg = msg
        self.name = name

    def __del__(self):
        print('デストラクタ起動')
        print(f'name={self.name}')

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var = SampleClass('Hello','taro')
var.print_msg()
var.print_name()
del var