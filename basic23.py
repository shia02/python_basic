#sub ジェネレーター
def sub_sub_generator():
    yield "sub sub yield"
    return "sub sub return"

def sub_generator():
    yield "sub yield"
    res = yield from sub_sub_generator()
    print(f'sub res = {res}')
    return "sub return"

def generator():
    yield "generator yield"
    res = yield from sub_generator()
    print(f'gen ges = {res}')
    return "generator return"


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))