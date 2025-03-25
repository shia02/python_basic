#例外
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(e,'0で割れない')
else: #例外が発生しないと動作する
    print('else処理')
finally: #必ず実行される
    print('finally')

try:
    b = []
    b.method()
except Exception as e:
    print(e)


class MyException(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise MyException('0で割れない')
    else:
        return a / b
try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))