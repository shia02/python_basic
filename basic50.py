#python 3.11

#Exception Group

def raise_exception():
    exceptions = []
    try:
        num = 10 / 0 #ZeroDivisionError
    except ZeroDivisionError as e:
        exceptions.append(e)

    try:
        msg = 'Hello' + 0
    except TypeError as e:
        e.add_note('type error 発生')
        exceptions.append(e)

    if len(exceptions) > 0:
        raise ExceptionGroup('例外発生', exceptions)

try:
    raise_exception()
except ExceptionGroup as eg:
    import traceback
    traceback.print_exception(eg)
    print(eg)
print('aaa')

