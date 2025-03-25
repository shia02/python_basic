#関数
def print_hello():
    print('hello')

def num_max(a, b):
    if a > b:
        return a
    else:
        return b
    
def sample(arg1, arg2=100):
    print(arg1, arg2)

def spam(arg1,*arg2):
    print(f'arg1 = {arg1}, arg2 = {arg2}')
    print(type(arg2))

def spam2(arg1, **arg2):
    print(f'arg1 = {arg1}, arg2 = {arg2}')
    print(type(arg2))

print_hello()
print(num_max(2,4))
sample(100)
sample(100,200)
spam(1,2,4,5,6)
spam2(1, name='tara', age=20)