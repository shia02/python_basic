#高階関数
def print_hello():
    print('hello')

def print_goodbye():
    print('goodbye')

var = ['aa', print_hello, print_goodbye]
var[2]()
var[1]()

def print_world(msg):
    print(f'{msg} world')

def print_konitiwa():
    print('こんにちは')

def print_hello(func):
    func('hello')
    return print_konitiwa

var = print_hello(print_world)
var()